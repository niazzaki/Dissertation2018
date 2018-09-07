FROM node

RUN npm install pushsafer-notifications

ADD NodeJServer.js  /usr/src/node/NodeJServer.js

ADD PushMessage.js /usr/src/node/PushMessage.js

EXPOSE  3001

WORKDIR /usr/src/node

CMD node NodeJServer.js
