<template>
    <h1>Settings</h1>
    <el-form :model="form" label-width="180px">
        <el-form-item label="Meilisearch url">
            <el-input v-model="form.url" />
        </el-form-item>
        <el-form-item label="Meilisearch api key">
            <el-input v-model="form.apiKey" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Save</el-button>
        </el-form-item>
    </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { State } from '~/composables/state';
import StateKey from '~/composables/stateKey'

const { update } = inject(StateKey) as State
const form = reactive({
    url: '',
    apiKey: ''
})

const onSubmit = () => {
    update(form.url, form.apiKey)
}
</script>