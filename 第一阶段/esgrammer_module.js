function main({ product_info }) {
  // 解析 JSON 字符串
  const parsedData = JSON.parse(product_info);

  // 获取 'result' 数组
  const resultArray = parsedData.result;

  // 存储遍历时的结果
  const resultList = [];

  // 遍历 resultArray
  resultArray.forEach(item => {
      console.log(item);  // 打印每一个元素
  });

  // 返回结果列表
  return resultArray;
}

let data = {
  "product_info": "{\"data\":[{\"Product_ID\":1,\"Product_Number\":\"S4SS1067\",\"Product_Name\":\"小冰纱防晒外套\",\"brand_id\":1},{\"Product_ID\":2,\"Product_Number\":\"S3AW1066\",\"Product_Name\":\"无缝拼接鹅绒外套\",\"brand_id\":1}]}",
  "userInput": "1sadsd"
}
;

let result_list = main(data);

console.log(result_list)