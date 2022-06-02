<template>
  <div class="outer-wrapper">
    <div class="input-wrapper">
      <Textarea v-model="urls"/>
      <ProgressSpinner v-if="isLoading" />
      <Button @click="getData" v-else>get data</Button>
    </div>
    <div class="results-wrapper" v-if="results.length > 0">
      RESULTS
      <DataTable :value="results">
        <Column field="asin" header="ASIN" />
        <Column field="item_name" header="Name" />
        <Column field="bullet_point" header="Bullet Points">
          <template #body="slotProps">
            <ul>
              <li v-for="li, i in slotProps.data.bullet_point" :key="i">{{li}}</li>
            </ul>
          </template>
        </Column>
        <Column field="images" header="Images">
          <template #body="slotProps">
            <span v-for="img, i in slotProps.data.images" :key="i">
              <img :src="img" class="data-image" />
            </span>
          </template>
        </Column>
        <Column field="image_count" header="Number of Images" />
        <Column field="product_details" header="Details" />
      </DataTable> 
    </div>
  </div>
</template>

<script>
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';


export default {
  components: {
    Textarea,
    Button,
    ProgressSpinner,
    DataTable,
    Column
  },
  data() {
    return {
      urls: '',
      results: [{
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
}],
  isLoading: false
    };
  },
  methods: {
    async getData() {
      this.isLoading = true
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
        this.results.push(response.data.items[0]);
      }
      this.isLoading = false;
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
.results-wrapper {
  display: flex;
  flex-direction: column;
}
.input-wrapper > textarea {
  height: 200px;
}

.input-wrapper > button {
  width: 50%;
  align-self: center;
}

.data-image {
  width: 50px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)
}

</style>