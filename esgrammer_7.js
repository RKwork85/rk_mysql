function main({ data1, userInput }) {
    // 解析 JSON 字符串
    const resultArray = JSON.parse(data1);
  
    // 尝试将 userInput 转换为整数
    const parsedInput = parseInt(userInput, 10);
  
    // 定义一个变量来存储找到的数据
    let foundData = null;
  
    if (!isNaN(parsedInput)) {
      // 如果转换成功，则在 Product_ID 中查找匹配项
      foundData = resultArray.find(item => item.Product_ID === parsedInput);
    } else {
      // 如果转换失败，则在 Product_Name 中查找匹配项
      foundData = resultArray.find(item => item.Product_Name === userInput);
    }
  
    // 返回查找结果
    if (foundData) {
      return { findData: foundData };
    } else {
      return { unfind: "没有该数据" };
    }
  }
  
  // 示例数据
  const data = {
    data1: JSON.stringify([
      { Product_ID: 1, Product_Number: 'S4SS1067', Product_Name: '小冰纱防晒外套', brand_id: 1 },
      { Product_ID: 2, Product_Number: 'S3AW1066', Product_Name: '无缝拼接鹅绒外套', brand_id: 1 }
    ])
  };
  
  // 测试函数
  console.log(main({ data1: data.data1, userInput: '1' }));         // 应返回 { finddata: {...} }
  console.log(main({ data1: data.data1, userInput: '小冰纱防晒外套' })); // 应返回 { finddata: {...} }
  console.log(main({ data1: data.data1, userInput: '不存在的数据' }));    // 应返回 { unfind: "没有该数据" }

  