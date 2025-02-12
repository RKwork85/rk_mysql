const data = {
    "data1": "{\"result\":[{\"ID\":5,\"Product_Color\":\"森林绿\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":6,\"Product_Color\":\"火山灰\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":7,\"Product_Color\":\"曜石黑\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":8,\"Product_Color\":\"暗夜红\",\"Tag\":\"颜色\",\"Card\":2}]}"
  }


  function hhh({data1, Product_Name}){
    let data = JSON.parse(data1)
    data.result.forEach((value, index) =>{
        console.log(index, value )
    })
  }

  hhh(data)  一次循环的输出值为，0 { ID: 5, Product_Color: '森林绿', Tag: '颜色', Card: 2 }， hhh(data)为这个代码添加逻辑，