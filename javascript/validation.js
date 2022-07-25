function checkfname()
{
    var f=document.frm.fname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        document.getElementById("fname").innerHTML="please enter the first name";
    }
    else if(!reg.test(f))
    {
        document.getElementById("fname").innerHTML="please enter only alphabets"; 
    }
    else
    {
        document.getElementById("fname").innerHTML=""; 
    }
}
function checklname()
{
    var f=document.frm.lname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        document.getElementById("lname").innerHTML="please enter the last name";
    }
    else if(!reg.test(f))
    {
        document.getElementById("lname").innerHTML="please enter only alphabets"; 
    }
    else
    {
        document.getElementById("lname").innerHTML=""; 
    }
}
function checkemail()
{
    var f=document.frm.fname.value;
    var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
    if(f=="")
    {
        document.getElementById("email").innerHTML="please enter email";
    }
    else if(!reg.test(f))
    {
        document.getElementById("email").innerHTML="please enter valid email"; 
    }
    else
    {
        document.getElementById("email").innerHTML=""; 
    }
}
function checkmobile()
{
    var f=document.frm.mobile.value;
    var reg=/^\d{10}$/;
    if(f=="")
    {
        document.getElementById("mobile").innerHTML="please enter mobile no";
    }
    else if(!reg.test(f))
    {
        document.getElementById("mobile").innerHTML="please enter valid mobile no"; 
    }
    else
    {
        document.getElementById("mobile").innerHTML=""; 
    }
}
function checkpassword()
{
    var f=document.frm.password.value;
    var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if(f=="")
    {
        document.getElementById("password").innerHTML="please enter password";
    }
    else if(!reg.test(f))
    {
        document.getElementById("password").innerHTML="please enter valid password"; 
    }
    else
    {
        document.getElementById("password").innerHTML=""; 
    }
}
function checkcpassword()
{
    var p1=document.frm.password.value;
    var p2=document.frm.cpassword.value;
    
    if(p2=="")
    {
        document.getElementById("cpassword").innerHTML="please enter confirm password";
    }
    else if(p1!=p2)
    {
        document.getElementById("cpassword").innerHTML="password & conform password does not match"; 
    }
    else
    {
        document.getElementById("cpassword").innerHTML=""; 
    }
}