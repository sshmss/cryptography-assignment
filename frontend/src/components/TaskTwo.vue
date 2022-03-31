<template>
  <div>
    <v-container class="ma-12">
      <v-row>
        <v-col cols="6">
          <div class="title mb-8">BCH Code Generation and Error correction</div>
          <v-text-field v-model="card_no" label="(10, 6)" outlined></v-text-field>
          <v-card-actions class="px-0">
            <v-spacer></v-spacer>
            <v-btn depressed color="primary" x-large> Submit </v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaskOne",
  data() {
    return {
      card_no: null,
      response: null,
    };
  },
  methods: {
    postCard() {
      const path = "http://localhost:5000/task1";
      axios
        .post(path, this.card_no)
        .then((res) => {
          this.response = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
