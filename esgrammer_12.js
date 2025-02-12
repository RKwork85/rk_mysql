const data = {
    "data1": "{\"result\":[{\"ID\":5,\"Product_Color\":\"森林绿\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":6,\"Product_Color\":\"火山灰\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":7,\"Product_Color\":\"曜石黑\",\"Tag\":\"颜色\",\"Card\":2},{\"ID\":8,\"Product_Color\":\"暗夜红\",\"Tag\":\"颜色\",\"Card\":2}]}"
  };
  
  function main({ data1, Product_Name }) {
    let parsedData = JSON.parse(data1);
    let mdTable = `| 颜色ID | ${Product_Name} |\n|--------|----------------|\n`;
  
    parsedData.result.forEach((value, index) => {
      mdTable += `| ${index + 1} | ${value.Product_Color} |\n`;
    });
  
    console.log(mdTable);
  }
  
  hhh(data);