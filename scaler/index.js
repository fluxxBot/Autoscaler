const { count } = require("./count");
const { createDeployment } = require("./createDeployment");
const { scale } = require("./scale");
const fs = require("fs");

const outputDataDir = "../predictive_optimiser/output.txt";

const outputData = fs.readFileSync(outputDataDir);

if (!outputData) {
  console.error("No output data found");
  return;
}

const totalRequiredInstance = parseInt(outputData, 10);
const availableInstance = count("onebox");

availableInstance.then((result) => {
  const requiredInstances = totalRequiredInstance - result;

  if (result === 0) {
    createDeployment("onebox", () => {
      scale(totalRequiredInstance, "onebox");
    });
  } else if (requiredInstances > 0) {
    scale(totalRequiredInstance, "onebox");
  } else {
    const toScaleDown = result + requiredInstances;
    if (toScaleDown <= 0) {
      console.error("No instances to scale down");
      return;
    }
    scale(toScaleDown, "onebox");
  }
  fs.writeFileSync(outputDataDir, '');
});
