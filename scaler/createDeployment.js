const { deploymentSpec } = require("./deploymentSpec");
const yaml = require('js-yaml');
const fs = require('fs');
const { exec } = require('node:child_process');

function createDeployment (namespace, callback) {
  const deploymentSpecYaml = yaml.dump(deploymentSpec);
  fs.writeFileSync('./deployment.yaml', deploymentSpecYaml);

  exec(`kubectl apply -f deployment.yaml -n ${namespace}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing command: ${error.message}`);
      return;
    }
  
    if (stderr) {
      console.warn(`stderr: ${stderr}`);
      return;
    }
  
    console.log(`stdout: ${stdout}`);
    fs.unlinkSync('./deployment.yaml');
    callback();
  });
}

module.exports = { createDeployment };