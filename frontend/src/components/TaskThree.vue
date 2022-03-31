<template>
  <div>
    <v-container class="ma-12">
      <v-row>
        <v-col cols="6">
          <div class="title mb-8">Brute forcing a password</div>
          <v-text-field
            v-model="password"
            label="Enter a password (max: 6) (lowercase letters and numbers only)"
            outlined
            :rules="passwordRules"
          ></v-text-field>
          <v-card-actions class="px-0">
            <v-spacer></v-spacer>
            <v-btn depressed color="primary" x-large @click="bruteForce" :loading="matching">
              Submit
            </v-btn>
          </v-card-actions>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          {{ match }}
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
      password: null,
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) => v.length <= 6 || "Password must be less than or equal to 6 characters",
      ],
      response: null,
      snackbarError: false,
      snackbarSuccess: false,
      error: null,
      match: "",
      matching: false,
    };
  },
  methods: {
    bruteForce() {
      this.matching = true;
      const path = "http://localhost:5000/task3";
      axios
        .post(path, JSON.stringify({ password: this.password }), {
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
        })
        .finally(() => {
          this.matching = false;
        });
    },
  },
  created() {},
};
</script>
