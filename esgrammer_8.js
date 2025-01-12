function main({ product_info, userInput }) {
    // 解析 JSON 字符串
    const resultArray = JSON.parse(product_info);
    console.log(resultArray.data)
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
  