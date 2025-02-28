// 重要


function main({ templateListMarketing, data, quanjubianliang}) {
    console.log(quanjubianliang.length)
    if (!quanjubianliang.length){
    console.log('hhh,全局变量不空的！')
    quanjubianliang.forEach((template, index) => {
      if (index < data.length) {
        // 解析出当前 data 的 JSON 对象
        const parsedData = JSON.parse(data[index]);
  
        // 遍历每个 JSON 对象中的值
        Object.values(parsedData).forEach(copy => {
            console.log(index, copy)
          // 将值添加到 copywriter 列表中
          template.copywriter.push(copy);
        });
      }
  
    })
    return {upgradeData:quanjubianliang};
  
  } else{
    console.log('全局变量为空的！')
    // 全局变量为空的逻辑
    // 遍历 templateListMarketing 列表
    templateListMarketing.forEach((template, index) => {
      // 如果 copywriter 属性不存在，则初始化为空列表
      if (!template.copywriter) {
        template.copywriter = [];
      }
      // 检查 data 索引是否存在于 data 数组中
      if (index < data.length) {
        // 解析出当前 data 的 JSON 对象
        const parsedData = JSON.parse(data[index]);
  
        // 遍历每个 JSON 对象中的值
        Object.values(parsedData).forEach(copy => {
            console.log(index, copy)
          // 将值添加到 copywriter 列表中
          template.copywriter.push(copy);
        });
      }
    });
    // 输出结果以查看修改后的 templateListMarketing
    return {upgradeData:templateListMarketing};
  }
  }