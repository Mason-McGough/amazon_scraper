<template>
  <div>
    <div>
      <textarea v-model="urls"/>
      <button @click="getData">get data</button>
    </div>
    <div v-if="results.length > 0">
      RESULTS
      <div v-for="(result, i) in results" :key="i">
        <label for="result">{{ i }}</label>
        <div>
          <pre>
            {{ result }}
          </pre>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      urls: '',
      results: [],
    };
  },
  methods: {
    addProduct() {
      this.urls.push({url: ''})
    },
    async getData() {
      let products = this.urls.split(',')
      console.log(products)
      let responses = [];
      for (let i = 0; i < products.length; i++) {
        const url = products[i].trim();
        console.log(url)
        let response = await this.axios.post(
          "http://localhost:9080/crawl.json?spider_name=amazon",
          {
            request: {
              url: url,
            },
            spider_name: "amazon",
          }, {
            headers: {
              'Content-type': 'application/x-www-form-urlencoded'
            }
          }
        );
        console.log(response)
        responses.push(response.data.items);
      }
      this.results = responses;
    },
  },
};
</script>
