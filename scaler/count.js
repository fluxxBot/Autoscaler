const { exec } = require('node:child_process');

function count(namespace) {
  return new Promise((resolve, reject) => {
    exec(`kubectl get deployment nginx-deployment -n ${namespace} -o json | jq '.spec.replicas'`, 
      (error, stdout, stderr) => {
        if (error) {
          reject(error);
          return;
        }
      
        if (stderr) {
          reject(new Error(stderr));
          return;
        }
      
      const count = parseInt(stdout.trim(), 10);
      resolve(count);
    });
  });
}

module.exports = { count };
