import "./ViewGroup.scss";

function ViewGroup() {
  return (
    <div className="view-group">
      <p className="view-group-title">view</p>
      <div className="view-group-btns">
        <div className="view-btn">%</div>
        <div className="view-btn">k</div>
        <div className="view-btn">n</div>
      </div>
    </div>
  );
}

export default ViewGroup;
