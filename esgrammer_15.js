data = {
    "data1": "12"
  }


function main({data1}){

    // let str = "12";
    let num = parseInt(data1);
    console.log(num ,typeof num); // 输出：12

}

main(data)



function main({}){
    const hhh=["","开始执行","开始执行"]

    return {
        inputList: hhh

    }

}


// 假设输入的字符串是str
let str = "hello";

// 定义一个空数组
let arr = [];

// 循环十次，将字符串str添加到数组中
for(let i = 0; i < 10; i++){
    arr.push(str);
}

data={
    data1:str
}
console.log(arr);

function main1({data1}){
    const inputStr  = data1
    const inputArr = []
    for(let i =0; i<10; i++){
        inputArr.push(inputStr)
    }

    return {ProductInputInfo: inputArr}
}

console.log(main1(data).inputArr)


