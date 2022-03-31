<template>
  <div>
    <v-container class="ma-12">
      <v-row>
        <v-col cols="6">
          <div class="title mb-8">Credit Card Verification</div>
          <v-text-field v-model="card_no" label="Card Number" outlined></v-text-field>
          <v-card-actions class="px-0">
            <v-spacer></v-spacer>
            <v-btn depressed color="primary" x-large @click="postCard()"> Submit </v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
    </v-container>
    <v-snackbar v-model="snackbarError" color="red darken-4">
      {{ error }}

      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbarError = false"> Close </v-btn>
      </template>
    </v-snackbar>
    <v-snackbar v-model="snackbarSuccess">
      {{ response }}

      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="snackbarSuccess = false"> Close </v-btn>
      </template>
    </v-snackbar>
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
      error: null,
      snackbarError: false,
      snackbarSuccess: false,
    };
  },
  methods: {
    postCard() {
      const path = "http://localhost:5000/task1";

      axios
        .post(path, JSON.stringify({ card_no: this.card_no }), {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          this.response = res.data.data;
          this.snackbarSuccess = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.error = error.response.data.data;
          this.snackbarError = true;
        });
    },
  },
  created() {},
};
</script>
