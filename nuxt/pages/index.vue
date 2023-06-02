<template>
    <div class="common-layout">
        <el-container>
            <el-aside>
                <h5 class="mb-2">Try Meilisearch</h5>
                <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
                    <el-menu-item index="1" @click="moveSettings">
                        <el-icon>
                            <setting />
                        </el-icon>
                        <span>Settings</span>
                    </el-menu-item>
                    <el-menu-item index="2" @click="moveSearch">
                        <el-icon><icon-menu /></el-icon>
                        <span>Search</span>
                    </el-menu-item>
                    <el-menu-item index="3" @click="moveIndexes">
                        <el-icon>
                            <setting />
                        </el-icon>
                        <span>Indexes</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-main>
                <keep-alive>
                    <component :is="currentComponent"></component>
                </keep-alive>
            </el-main>
        </el-container>
    </div>
</template>

<script lang="ts" setup>
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'
import Settings from '~/components/Settings.vue'
import Search from '~/components/Search.vue'
import Indexes from '~/components/Indexes.vue'

const currentComponent = ref(Settings)
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}

const moveSettings = () => {
    currentComponent.value = Settings
}
const moveSearch = () => {
    currentComponent.value = Search
}

const moveIndexes = () => {
    currentComponent.value = Indexes
}
</script>