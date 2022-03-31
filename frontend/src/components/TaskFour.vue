<template>
  <div>
    <v-container class="ma-12">
      <v-row>
        <v-col cols="8">
          <div class="title mb-8">Rainbow Tables</div>
          <v-row>
            <v-col>
              <v-text-field
                v-model="possible_inputs"
                label="Possible inputs"
                :rules="inputRules"
                outlined
              ></v-text-field>
            </v-col>
            <v-col>
              <v-text-field
                v-model="hash"
                :rules="hashRules"
                label="Hash containing possible inputs"
                outlined
              >
              </v-text-field>
            </v-col>
          </v-row>
          <v-card-actions class="px-0 mb-8">
            <v-spacer></v-spacer>
            <v-btn x-large :loading="loading" :disabled="loading" color="success" @click="crack">
              Crack
              <template v-slot:loader>
                <span>Cracking</span>
              </template>
            </v-btn>
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
      possible_inputs: null,
      inputRules: [
        (v) => !!v || "Input is required",
        (v) => v.length <= 9 || "Input must be less than 9 characters",
      ],
      hash: null,
      hashRules: [
        (v) => !!v || "Hash is required",
        (v) => v.length <= 9 || "Hash must be less than 9 characters",
      ],
      loading: false,
      response: null,
      error: null,
      snackbarError: false,
      snackbarSuccess: false,
    };
  },
  methods: {
    crack() {
      if (this.hash.length !== this.possible_inputs.length) {
        this.snackbarError = true;
        this.error = "Length of hash must be same as possible inputs";
        return;
      }
      this.loading = true;
      const path = "http://localhost:5000/task4";

      axios
        .post(path, JSON.stringify({ possible_inputs: this.possible_inputs, hash: this.hash }), {
          headers: { "Content-Type": "application/json" },
        })
        .then((res) => {
          this.response = res.data.data;
          this.loading = false;
          this.snackbarSuccess = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          this.loading = false;
          this.error = error.response.data.data;
          this.snackbarError = true;
        });
    },
  },
};
</script>
<style>
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
</style>
