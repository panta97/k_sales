import os
import re
from xmlrpc import client as xmlrpclib


def lambda_handler(event, context):

    # GET ENVIRONMENT VARIABLES
    url = os.environ["URL"]
    db = os.environ["DB"]
    pwd = os.environ["PWD"]
    uid = int(os.environ["UID"])

    # GET PURCHASE ORDER ID FROM GATEWAY API
    date = event["date"]

    # GET ACCOUNT INVOICES
    invoice_filter = [
        [
            ["date_invoice", "=", date],
            ["state", "in", ["paid", "open"]],
            ["type", "in", ["out_invoice", "out_refund"]],
        ]
    ]
    invoice_fields = ["journal_id", "amount_total", "company_id"]
    models = xmlrpclib.ServerProxy("{}/xmlrpc/2/object".format(url))
    invoices = models.execute_kw(
        db,
        uid,
        pwd,
        "account.invoice",
        "search_read",
        invoice_filter,
        {"fields": invoice_fields, "context": {"lang": "es_PE"}},
    )

    total_ab = 0
    total_sm = 0
    total_ol = 0

    for invoice in invoices:
        serie = re.search("^.+([B|F][A|0]0\d).+$", invoice["journal_id"][1]).group(1)
        company_id = invoice["company_id"][0]

        if company_id == 1:  ## kdosh
            if serie in [
                "B001",
                "B003",
                "B004",
                "B005",
                "B006",
                "F001",
                "F003",
                "F004",
                "F005",
            ]:
                total_ab += invoice["amount_total"]
            elif serie in ["B002", "F002"]:
                total_sm += invoice["amount_total"]
            elif serie == "BA01":
                total_ab -= invoice["amount_total"]
            elif serie == "BA02":
                total_sm -= invoice["amount_total"]
        elif company_id == 3:  ## olympo
            total_ol += invoice["amount_total"]

    totals = [
        {
            "code": "ab-store",
            "name": "abtao",
            "amount": total_ab,
        },
        {
            "code": "sm-store",
            "name": "san martin",
            "amount": total_sm,
        },
        {
            "code": "ol-store",
            "name": "olympo",
            "amount": total_ol,
        },
    ]

    return {
        "statusCode": 200,
        "body": totals,
    }


lambda_handler(None, None)
