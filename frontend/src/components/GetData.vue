<template>
  <div class="outer-wrapper">
    <div class="input-wrapper">
      <Textarea v-model="urls" />
      <ProgressSpinner v-if="isLoading" />
      <Button @click="getData" v-else>get data</Button>
    </div>
    <div class="results-wrapper" v-if="results.length > 0">
      RESULTS
      <DataTable :value="results" class="p-datatable-sm" dataKey="asin">
        <Column field="asin" header="ASIN" />
        <Column field="item_name" header="Name" />
        <Column field="bullet_point" header="Bullet Points">
          <template #body="slotProps">
            <ul>
              <li v-for="(li, i) in slotProps.data.bullet_point" :key="i">
                {{ li }}
              </li>
            </ul>
          </template>
        </Column>
        <Column field="images" header="Images">
          <template #body="slotProps">
            <span v-for="(img, i) in slotProps.data.images" :key="i">
              <img :src="img" class="data-image" />
            </span>
          </template>
        </Column>
        <Column field="image_count" header="Number of Images" />
        <Column field="product_details" header="Details">
          <template #body="slotProps">
            <table>
              <tr v-for="(li, i) in slotProps.data.product_details" :key="i">
                <th>{{ li.split(':')[0] }}</th>
                <td>{{ li.split(':')[1] }}</td>
              </tr>
            </table>
          </template>
        </Column>
        <Column field="props" header="Props">
          <template #body="slotProps">
            <ul>
              <li v-for="(li, i) in slotProps.data.props" :key="i">
                {{ li.name }}
              </li>
            </ul>
          </template>
        </Column>
        <Column field="lifestyle" header="Lifestyle">
          <template #body="slotProps">
            <ul>
              <li v-for="(li, i) in slotProps.data.lifestyle" :key="i">
                {{ li.name }}
              </li>
            </ul>
          </template>
        </Column>
        <Column field="packs" header="Packs">
          <template #body="slotProps">
            <ul>
              <li v-for="(li, i) in slotProps.data.packs" :key="i">
                {{ li.name }}
              </li>
            </ul>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import Textarea from "primevue/textarea";
import Button from "primevue/button";
import ProgressSpinner from "primevue/progressspinner";
import DataTable from "primevue/datatable";
import Column from "primevue/column";

export default {
  components: {
    Textarea,
    Button,
    ProgressSpinner,
    DataTable,
    Column,
  },
  data() {
    return {
      urls: "",
      results: [
        {
          asin: "B007R8XGJA",
          item_name:
            "CELSIUS Essential Energy Drink 12 Fl Oz, Sparkling Orange (Pack of 12)",
          bullet_point: [
            " Pre-Workout Drink  ",
            " Your Ultimate Fitness Partner  ",
            " Healthy Energy, 200 mg Caffeine.Gluten free  ",
            " Energy to Live Fit  ",
            " Zero Sugars, Zero Preservatives  ",
            " No Artificial Flavors or Colors  ",
            " Sparkling Orange, 12 oz. Slim Can  ",
            " Drink in the bathroom ",
          ],
          images: [
            "https://m.media-amazon.com/images/I/71py1NThZdL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/81+G6hdlCOL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/81O9Xj80wGL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71YguAQd9jL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71zqahvJcWL._SL1500_.jpg",
          ],
          image_count: 5,
          product_details: [
            "Manufacturer: Mantra Enterprise",
            "Part Number: B5155RB",
            "Item Weight: 15.2 ounces",
            "Package Dimensions: 4.37 x 3.31 x 2.68 inches",
            "Item model number: B5155RB",
            "Is Discontinued By Manufacturer: No",
            "Item Package Quantity: 1",
            "Number Of Holes: 2",
            "Batteries Included?: No",
            "Batteries Required?: No",
            "ASIN: B006X628BE",
            "Date First Available: January 13, 2012",
          ],
          props: [],
          lifestyle: [],
          packs: [{ name: "BEVERAGE"}],
        },
      ],
      isLoading: false,
      props: [
        { id: 1, name: "BATH TOWELS", keywords: ["bath", "bathroom", "towel"] },
        { id: 2, name: "CANDLE", keywords: ["cozy", "candle"] },
        { id: 3, name: "POTTED FERN" },
      ],
      lifestyle: [
        { id: 'flddr5G2wWLwoaN77', name: "BATHROOM", keywords: ["bath", "bathroom", "towel"] },
        { id: 'fldAuv5qIUg8bgbHz', name: "BEDROOM", keywords: ["bed", "bedroom", "sleep"]},
        { id: 'fldPM53EUkGB4GbEL', name: "E-COMM WHITE" },
        { id: 'fldi9OaPMdWzJrSDD', name: "ENTRY" },
        { id: 'fldhpPbwbUJHvk6Vb', name: "KITCHEN", keywords: ["kitchen", "cook", "cooking", "food", "grocery", "eat"]},
        { id: 'fldr5sZXPF4ogQrfB', name: "LAUNDRY", keywords: ["laundry"]},
        { id: 'fldhyGEpimNoNjn8A', name: "LIVINGROOM", keywords: ["sofa", "chair"] },
      ],
      packs: [
        { id: 1, name: "AMAZON" },
        { id: 2, name: "BEVERAGE", keywords: ["drink", "sparkling"] },
        { id: 3, name: "BEAUTY", keywords: ["beauty", "lipstick", "nails", "polish", "body", "moisturize"] },
        { id: 4, name: "PET", keywords: ["cat", "dog", "pet", "fido"]},
        { id: 5, name: "HEALTH", keywords: ["fitness", "exercise", "health", "self-care"] },
        { id: 6, name: "PRODUCT_VIDEO" },
        { id: 7, name: "HAND_MODEL_VIDEO", keywords: ["hand", "glove", "gloves", "hands", "nails", "polish"] },
        { id: 8, name: "MODEL_VIDEO", keywords: ["shirt", "pants", "shorts", "socks", "backpack", "wearable"] },
        { id: 9, name: "UNPACKING" },
      ],
    };
  },
  methods: {
    async getData() {
      this.isLoading = true;
      let products = this.urls.split("\n");
      console.log(products);
      for (let i = 0; i < products.length; i++) {
        const url = products[i].trim();
        let proxied_url = `http://api.scraperapi.com/?api_key=${
          import.meta.env.VITE_PROXY_API_KEY
        }&url=${url}`;
        let response = await this.axios.post(
          "http://localhost:9080/crawl.json?spider_name=amazon",
          {
            request: {
              url: proxied_url,
            },
            spider_name: "amazon",
          },
          {
            headers: {
              "Content-type": "application/x-www-form-urlencoded",
            },
          }
        );
        console.log(response);
        let product = { ...response.data.items[0] };
        this.results.push({
          ...product,
          props: this.assignTags(product, this.props),
          lifestyle: this.assignTags(product, this.lifestyle),
          packs: this.assignTags(product, this.packs)
        });
      }
      this.isLoading = false;
    },
    assignTags(product, category) {
      let category_matches = [];
      category.forEach((thing) => {
        let keyword_set = new Set(thing.keywords);
        let bullet_words = [];
        product.bullet_point.forEach((line) =>
          bullet_words.push(line.replace(/\p{P}/gu, "").split(" "))
        );
        bullet_words.forEach((line) => {
          let words = new Set(line);
          let matches = [...words].filter((x) => keyword_set.has(x));
          if (matches.length > 0) {
            category_matches.push(thing);
          }
        });
      });
      return category_matches;
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
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
</style>
