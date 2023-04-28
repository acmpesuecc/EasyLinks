const express= require("express");
const app =express()
app.use(express.static("public"));

app.get("/",function(request,responce){
    response.sendFile(__dirname + "/redirecthome.html");

});

app.listen(5000);