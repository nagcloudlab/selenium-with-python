
//----------------------------------------
// using DOM api
//----------------------------------------

const input1Ele=document.getElementById("input1");
const input2Ele=document.getElementById("input2");
const operationEle=document.getElementById("operation");
const calculateBtnEle=document.getElementById("calculate");
const resultEle=document.getElementById("result");


calculateBtnEle.addEventListener("click",function(){
    const input1=input1Ele.value;
    const input2=input2Ele.value;
    const operation=operationEle.value;
    console.log(operation);

    let result;
    if(operation=="+"){
        result=parseInt(input1)+parseInt(input2);
    }else if(operation=="-"){
        result=parseInt(input1)-parseInt(input2);
    }else if(operation=="+"){
        result=parseInt(input1)*parseInt(input2);
    }else if(operation=="/"){
        result=parseInt(input1)/parseInt(input2);
    }else{
        result="Invalid Operation";
    }

    resultEle.innerText=result;
});