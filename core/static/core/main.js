var apiUrl = "https://h3241a1966.zicp.fun/family/menu/"; // 这是您的 API 端点，用于获取 menu 数据
$.get(apiUrl, function(data) {
    // 在请求成功时，data 包含从服务器获取的 menu 数据
    // 确保您的 API 返回的数据结构与 menu 对象相匹配

    console.log("数据获取成功：", data); // 输出数据到控制台，以供调试

    // 检查数据是否有效，例如是否有数据
    if (data) {
        // 获取容器元素
        var menuData = data[0]; // 假设 data 是一个包含在数组中的对象

        var menuContainer = document.getElementById("menu-container");
        var menuTitleElement = document.getElementById("menu-title");
        var menuDescriptionElement = document.getElementById("menu-description");
        var menuChefElement = document.getElementById("menu-chef");
        var menuImageElement = document.createElement("img");

        // 将数据填充到容器中
        menuTitleElement.textContent = menuData.title;
        menuDescriptionElement.textContent = menuData.description;
        menuChefElement.textContent = "主厨: " + menuData.chef.username; // 假设 chef 数据中有一个名为 name 的字段

        // 设置图片元素的 src 属性
        menuImageElement.src = menuData.images.image; // 假设 images 对象中有一个名为 image 的字段
        // 将图片元素添加到容器
        menuContainer.appendChild(menuImageElement);
    } else {
        console.log("数据为空或无效"); // 输出错误信息到控制台
    }
}).fail(function() {
    console.log("获取数据失败"); // 输出错误信息到控制台
});
