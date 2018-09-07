var push = require( 'pushsafer-notifications' );
module.exports=function(){ 

    var p = new push( {
    k: 'X00pU05cM7Sovd2SNAbo',             // your 20 chars long private key 
    debug: true
});
 
this.prepareMsg=function(data){
    d=JSON.stringify(data);
    var msg = {
        m: d,   // message (required)
        t: "Alert",                     // title (optional)
        s: '8',                                // sound (value 0-50) 
        v: '2',                                // vibration (empty or value 1-3) 
        i: '5',                                // icon (value 1-176)
        c: '#FF0000',                          // iconcolor (optional)
        u: 'https://www.pushsafer.com',        // url (optional)
        ut: 'Updates',                       // url title (optional)
        d: '12188'                               // the device or device group id 
    };
    console.log(msg);
    pushData(msg)
} 
 
this.pushData=function(msg){
    p.send( msg, function( err, result ) {

        console.log( 'RESULT', result );
        // process.exit(0); 
        })
    }
};
