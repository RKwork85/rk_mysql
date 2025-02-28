function main({ data1 }) {
  // 解析 JSON 字符串
  const parsedData = JSON.parse(data1);

  // 获取 'result' 数组
  const resultArray = parsedData.result;

  // 存储遍历时的结果
  const resultList = [];

  // 遍历 resultArray
  resultArray.forEach(item => {
      const {Product_Name, ...other} = item
      resultList.push(other)
      console.log('解构出来的产品名', Product_Name)
      console.log(other)

      // console.log(item);  // 打印每一个元素
  });
  resultList.forEach(item =>{
    console.log(item.Product_ID)
  })
  // 返回结果列表
  return resultArray;
}

let data = {
  "data1": "{\"result\":[{\"Product_ID\":1,\"Product_Name\":\"小冰纱防晒外套\",\"brand_id\":1},{\"Product_ID\":2,\"Product_Name\":\"无缝拼接鹅绒外套\",\"brand_id\":1}]}"
};

let result_list = main(data);

console.log(result_list)