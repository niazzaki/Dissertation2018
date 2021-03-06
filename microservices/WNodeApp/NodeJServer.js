const http = require('http');
require('./PushMessage')();
http.createServer((request, response) => {
  const { headers, method, url } = request;
  let body = [];
  request.on('error', (err) => {
    console.error(err);
  }).on('data', (chunk) => {
    body.push(chunk);
    
  }).on('end', () => {
    body = Buffer.concat(body).toString();
    response.on('error', (err) => {
      console.error(err);
    });

    response.statusCode = 200;
    response.setHeader('Content-Type', 'application/json');
    const responseBody = { headers, method, url, body };
    prepareMsg(responseBody.body);
    console.log(JSON.stringify(responseBody.body));
    response.write(JSON.stringify(responseBody.body));
    response.end();
  });
}).listen(3000);
