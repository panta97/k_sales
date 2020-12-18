function now() {
  const currTime = new Date();
  const minutes = String(currTime.getMinutes()).padStart(2, '0');
  const hours = String(currTime.getHours()).padStart(2, '0');
  return `${minutes}:${hours}`;
}

export default now;
