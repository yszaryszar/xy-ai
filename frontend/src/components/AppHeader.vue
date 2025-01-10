<script setup lang="ts">
import { ref } from 'vue'
import { Briefcase, Edit, HomeFilled, Tickets } from '@element-plus/icons-vue'
import SvgIcon from '@/components/SvgIcon.vue'

// 定义一个响应式变量 input，用于存储输入框的值
const input = ref('')
</script>

<template>
  <el-row
    class="container flex items-center !h-full max-w-screen-xl !m-auto"
    justify="center"
    :gutter="20"
  >
    <!-- 网站名称 -->
    <el-col :span="4">
      <a href="/" class="flex items-center">
        <h1 class="text-3xl font-bold">新语AI</h1>
        <img src="/logo.svg" alt="logo" class="ml-2 h-10" />
      </a>
    </el-col>

    <!-- 菜单栏 -->
    <el-col :span="16" class="h-full">
      <el-menu mode="horizontal" active-text-color="#009A61" class="flex-grow !h-full">
        <el-menu-item index="1">
          <svg-icon icon-class="AIxiezuo-moren" class="mr-1 !text-center !align-middle" />
          首页
        </el-menu-item>
        <el-menu-item index="2"
          ><el-icon><Edit /></el-icon>AI写作</el-menu-item
        >
        <el-menu-item index="3"
          ><el-icon><Briefcase /></el-icon>AI工具</el-menu-item
        >
        <el-menu-item index="4"
          ><el-icon><Tickets /></el-icon>AI资讯</el-menu-item
        >
        <el-menu-item index="5"
          ><el-icon><InfoFilled /></el-icon>关于本站</el-menu-item
        >
      </el-menu>
    </el-col>

    <!-- 登录和注册按钮 -->
    <el-col :span="4" class="flex justify-end space-x-4">
      <el-button round>登录</el-button>
      <el-button round>注册</el-button>
    </el-col>
  </el-row>
</template>

<style scoped>
.el-menu {
  border-bottom: none; /* 去掉底部边框 */
  height: 100%; /* 设置高度为100% */
  background-color: transparent; /* 设置背景色为透明 */
}

.el-menu-item {
  font-size: 18px; /* 设置字体大小 */
  font-weight: bold; /* 设置字体加粗 */
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  height: 100%; /* 填充菜单栏高度 */
}

.el-menu-item.is-active,
.el-menu-item:hover {
  background-color: #e1f3ec !important; /* 设置激活和悬停时的背景色 */
  color: #009a61 !important; /* 设置悬停时的字体颜色 */
}
</style>
