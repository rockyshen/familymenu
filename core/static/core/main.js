var apiUrl = "https://h3241a1966.zicp.fun/family/menu/"; // 这是您的 API 端点，用于获取 menu 数据

$.get(apiUrl, function (data) {
    // 在请求成功时，data 包含从服务器获取的 menu 数据
    // 确保您的 API 返回的数据结构与 menu 对象相匹配

    console.log("数据获取成功：", data); // 输出数据到控制台，以供调试

    // 检查数据是否有效，例如是否有数据
    if (data) {
        var menuContainer = document.getElementById("menu-container");

        for (var i = 0; i < data.length; i++) {
            // 获取容器元素
            var menuData = data[i]; // 假设 data 是一个包含在数组中的对象

            var menuDiv = document.createElement("div")
            menuDiv.classList.add("menu-item","card","card--primary"); // 添加类以标识每个菜单项

            var menuImageElement = document.createElement("img");
            var menuTitleElement = document.createElement("h2");
            var menuDescriptionElement = document.createElement("p");
            var menuChefElement = document.createElement("p");
            
            // 将数据填充到容器中
            menuTitleElement.textContent = menuData.title;
            menuTitleElement.classList.add("card__h2");
            menuDescriptionElement.textContent = menuData.description;
            menuDescriptionElement.classList.add("card__p");
            menuChefElement.textContent = "主厨: " + menuData.chef.username; // 假设 chef 数据中有一个名为 name 的字段
            menuChefElement.classList.add("card__p");
            menuImageElement.src = menuData.images.image;
            menuImageElement.classList.add("fixed-size-image");

            menuDiv.appendChild(menuImageElement); // 将子容器添加到 menuDiv 中
            menuDiv.appendChild(menuTitleElement);
            menuDiv.appendChild(menuDescriptionElement);
            menuDiv.appendChild(menuChefElement);
            menuContainer.appendChild(menuDiv);
        }
    } else {
        console.log("数据为空或无效"); // 输出错误信息到控制台
    }
}).fail(function () {
    console.log("获取数据失败"); // 输出错误信息到控制台
});
