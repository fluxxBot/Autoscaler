const { exec } = require('node:child_process');

function scale(replicaCount, namespace) {
  exec(`kubectl scale deployment/nginx-deployment --replicas=${replicaCount} -n ${namespace}`, 
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing command: ${error.message}`);
        return;
      }
    
      if (stderr) {
        console.warn(`stderr: ${stderr}`);
        return;
      }
    
      console.log(`stdout: ${stdout}`);
  });
}

module.exports = { scale };
