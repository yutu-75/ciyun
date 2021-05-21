<template>
  <div id="app">

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
 .el-color-picker__trigger {
  -webkit-box-sizing: border-box;
  height: 28px;
  width: 64px;
  padding: 4px;
  border-radius: 4px;
  font-size: 0;
  position: relative;
  cursor: pointer;
  vertical-align: middle;
  border: none;
}

.el-color-picker__icon {
  display: none;
}
</style>
