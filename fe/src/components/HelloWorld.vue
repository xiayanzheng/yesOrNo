<template>
  <div>
    <h1>{{ msg }}</h1>
    <van-row>
      <van-col span="8">
        <van-button round style="width: 20rem;height: 5rem" type="primary" @click="pushAnswer('yes')"><font
            size="5">Yes</font></van-button>
      </van-col>
      <van-col style="height: 2rem"></van-col>
      <van-col>
        <van-button round style="width: 20rem;height: 5rem" type="danger" @click="pushAnswer('no')"><font
            size="5">No</font></van-button>
      </van-col>
    </van-row>
  </div>
</template>

<script>
import Vue from 'vue';
import {Button} from 'vant';
import 'vant/lib/button/style';
import 'vant/lib/toast/style';
import {Col, Row} from 'vant';
import { Toast } from 'vant';

Vue.use(Col);
Vue.use(Row);
Vue.use(Button);
Vue.use(Toast);
export default {
  data() {
    return {
      isDev: false
    }
  },
  name: 'HelloWorld',
  components: {},
  props: {
    msg: String
  },
  methods: {
    pushAnswer(answerVal) {
      let url = window.location.origin + "/api/answer?answer="
      if (this.isDev) {
        url = "http://localhost:5000/api/answer?answer="
      }
      this.axios.get(url + answerVal + "&qid=q0001").then((response) => {
          console.log(response)
          Toast.success('提交成功');
        }).catch((response) => {
          console.log(response);
          Toast.fail('提交失败');
        })

    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
