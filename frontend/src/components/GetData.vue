<template>
  <div class="outer-wrapper">
    <div class="input-wrapper">
      <textarea v-model="urls"/>
      <button @click="getData">get data</button>
    </div>
    <div class="results-wrapper" v-if="results.length > 0">
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
      results: [`{
    "asin": "B007R8XGJA",
    "item_name": "CELSIUS Essential Energy Drink 12 Fl Oz, Sparkling Orange (Pack of 12)",
    "bullet_point": [
        " Pre-Workout Drink  ",
        " Your Ultimate Fitness Partner  ",
        " Healthy Energy, 200 mg Caffeine.Gluten free  ",
        " Energy to Live Fit  ",
        " Zero Sugars, Zero Preservatives  ",
        " No Artificial Flavors or Colors  ",
        " Sparkling Orange, 12 oz. Slim Can  "
    ],
    "images": [
        "https://m.media-amazon.com/images/I/71py1NThZdL._SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81+G6hdlCOL._SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81O9Xj80wGL._SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71YguAQd9jL._SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71zqahvJcWL._SL1500_.jpg"
    ],
    "image_count": 5
}`],
    };
  },
  methods: {
    addProduct() {
      this.urls.push({url: ''})
    },
    async getData() {
      let products = this.urls.split('\n')
      console.log(products)
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
        this.results.push(response.data.items);
      }
    },
  },
};
</script>

<style scoped>
.outer-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.input-wrapper {
  width: 50%;
  display: flex;
  flex-direction: column;
  row-gap: 1rem;
}

.input-wrapper > textarea {
  height: 200px;
}

.input-wrapper > button {
  width: 50%;
  align-self: center;
}

</style>