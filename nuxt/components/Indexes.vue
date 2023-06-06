<template>
    <h1>Indexes</h1>
    <el-form :model="form" label-width="140px">
        <el-form-item label="Index name">
            <el-input v-model="form.indexName" />
        </el-form-item>
        <el-form-item label="Query">
            <el-input v-model="form.query" />
        </el-form-item>
        <el-form-item label="Offest">
            <el-input-number v-model="form.offset" :min="1"  />
        </el-form-item>
        <el-form-item label="Limit">
            <el-input-number v-model="form.limit" :min="1"  />
        </el-form-item>
        <el-form-item label="hitsPerPage">
            <el-slider v-model="form.hitsPerPage" />
        </el-form-item>
        <el-form-item label="page">
            <el-input-number v-model="form.page" :min="1"  />
        </el-form-item>
        <el-form-item label="attributesToCrop">
            <el-input v-model="form.attributesToCrop" placeholder="Please input" />
        </el-form-item>
        <el-form-item label="AttributesToHighlight">
            <el-input v-model="form.attributesToHighlight" placeholder="Please input" />
        </el-form-item>
        <el-form-item label="HighlightPreTag">
            <el-input v-model="form.highlightPreTag" placeholder="<em>" />
        </el-form-item>
        <el-form-item label="HighlightPostTag">
            <el-input v-model="form.highlightPostTag" placeholder="</em>" />
        </el-form-item>
    </el-form>
    <div>
        <el-card class="box-card" v-for="result in results" :key="result.id">
            <el-row :gutter="20">
                <template v-for="(vValue, vKey) in getResultOrFormatted(result)" :key="vKey">
                    <el-col :span="6">
                        <span>{{ vKey }}</span>
                    </el-col>
                    <el-col :span="18">
                        <div class="text item">{{ vValue }}</div>
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
    query: '',
    offset: 0,
    limit: 20,
    hitsPerPage: 1,
    page: 1,
    attributesToCrop: '',
    attributesToHighlight: '',
    highlightPreTag: '<em>',
    highlightPostTag: '</em>'
})
const results = ref([])
const { state } = inject(StateKey) as State

const getResultOrFormatted = (r) => {
    return r.hasOwnProperty('_formatted') ? r._formatted : r
}

watch(form, async () => {
    const client = new MeiliSearch({ host: state.url, apiKey: state.apiKey })
    const index = client.index(form.indexName)
    const searchResults = await index.search(form.query, {
        offset: form.offset,
        limit: form.limit,
        hitsPerPage: form.hitsPerPage,
        page: form.page,
        attributesToCrop: form.attributesToCrop === '' ? ['*'] : form.attributesToCrop.split(','),
        attributesToHighlight: form.attributesToHighlight === '' ? ['*'] : form.attributesToHighlight.split(','),
        highlightPreTag: form.highlightPreTag,
        highlightPostTag: form.highlightPostTag
    })
    results.value = searchResults.hits as []
    console.log(searchResults)
})
</script>

<style scoped>
.box-card {
    margin-bottom: 25px;
}
</style>