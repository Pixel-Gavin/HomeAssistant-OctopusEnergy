const fs = require('fs');
const path = require('path');
const fileName = path.join(__dirname, '../custom_components/octopus_energy/manifest.json');
const file = require(fileName);

file.version = process.argv[2];
    
fs.writeFile(fileName, JSON.stringify(file, null, 2), function writeJSON(err) {
  return console.log(err);
});