import './Line.scss';

function Line({sales}) {
  const totalSales = sales.reduce((acc, curr) => acc += curr['amount'] , 0);
  const lineWidth = 260;
  return (
    <div className="line-percentage">
      {sales.map(({code, amount}) => (
        <div
          key={code}
          style={{'width': `${amount/totalSales * lineWidth}px`}}
          className={code}/>
      ))}
    </div>
  )
}

export default Line;
