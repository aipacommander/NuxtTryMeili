<template>
    <h1>Indexes</h1>
    <el-form :model="form" label-width="180px">
        <el-form-item label="Index name">
            <el-input v-model="form.indexName" />
        </el-form-item>
        <el-form-item label="query">
            <el-input v-model="form.query" />
        </el-form-item>
    </el-form>
    <div>
        <el-card class="box-card" v-for="result in results" :key="result.id">
            <template #header>
                <div class="card-header">
                    <span>{{ result.id }}</span>
                </div>
            </template>
            <el-row :gutter="20">
                <template v-for="k in Object.keys(result)" :key="k">
                    <el-col :span="6">
                        <span>{{ k }}</span>
                    </el-col>
                    <el-col :span="18">
                        <div class="text item">{{ result[k] }}</div>
                    </el-col>
                </template>
            </el-row>
        </el-card>
    </div>
    <pre>{{ results }}</pre>
</template>

<script setup lang="ts">
import MeiliSearch from 'meilisearch'
import { State } from '~/composables/state';
import StateKey from '~/composables/stateKey'

const form = reactive({
    indexName: '',
    query: ''
})
const results = ref([])
const { state } = inject(StateKey) as State

const { query } = toRefs(form)
watch(query, async () => {
    const client = new MeiliSearch({ host: state.url, apiKey: state.apiKey })
    const index = client.index(form.indexName)
    const searchResults = await index.search(form.query)
    results.value = searchResults.hits as []
    console.log(searchResults)
})
</script>

<style scoped>
.box-card {
    margin-bottom: 25px;
}
</style>