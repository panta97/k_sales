import Stores from "./Stores/Stores";
import ViewGroup from "./ViewGroup/ViewGroup";
import Reload from "./Reload/Reload";
import Line from "./Line/Line";
import './App.scss';


function App() {
  return (
    <div>
      <Reload/>
      <h1 className="main-title">sales of today</h1>
      <ViewGroup/>
      <Stores/>
      <Line/>
      <div className="line-deco"></div>
    </div>
  );
}

export default App;
