<script setup lang="ts">
import Header from '@/components/AppHeader.vue'
import Main from '@/components/MainContent.vue'
import Footer from '@/components/AppFooter.vue'
</script>

<template>
  <el-container class="bg-backgroundLight h-screen">
    <!-- Header -->
    <el-header class="bg-white text-primary !h-20 flex mb-2 shadow-md">
      <Header />
    </el-header>
    <!-- Main Content -->
    <el-main class="py-10 max-w-screen-xl m-auto items-stretch">
      <Main />
    </el-main>
    <!-- Footer -->
    <el-footer class="bg-gray-800 text-white text-center py-4">
      <Footer />
    </el-footer>
  </el-container>
</template>
