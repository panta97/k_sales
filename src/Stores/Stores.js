import './Stores.scss';
import StoreLine from "./StoreLine/StoreLine";

function Stores() {
    return (
      <div>
        <StoreLine
            bgColor={'ab-store'}
            storeName={'abtao'}
            salesAmount={9999}/>
        <StoreLine 
            bgColor={'sm-store'}
            storeName={'san martin'}
            salesAmount={999}/>
        <StoreLine 
            bgColor={'tt-store'}
            storeName={'total'}
            salesAmount={10998}/>
      </div>
    );
  }
  
  export default Stores;
  