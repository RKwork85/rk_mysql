const data = {
    "data1": "{\"result\":[{\"ID\":5,\"Product_Color\":\"森林绿\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":6,\"Product_Color\":\"火山灰\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":7,\"Product_Color\":\"曜石黑\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":8,\"Product_Color\":\"暗夜红\",\"Tag\":\"颜色\",\"Card\":2}]}"
  };
  
  function hhh({ data1, userInput }) {
    let parsedData = JSON.parse(data1);
    let result = { unfind: "没有颜色信息" };
  
    parsedData.result.forEach((value, index) => {
      if (String(index + 1) === userInput || value.Product_Color === userInput) {
        result = { findData: `${value.Tag}:${value.Product_Color}` };
      }
    });
  
    console.log(result);
  }
  
  // 测试用例
  hhh({ ...data, userInput: "森林绿" }); // { findData: "颜色:森林绿" }
  hhh({ ...data, userInput: "1" }); // { findData: "颜色:森林绿" }
  hhh({ ...data, userInput: "9" }); // { unfind: "没有颜色信息" }
  hhh({ ...data, userInput: "不存在的颜色" }); // { unfind: "没有颜色信息" }