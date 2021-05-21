<template>
  <div>
    <Header></Header>
    <div class="wordcloud">
      <el-row :gutter="0">
        <el-col :span="20" :offset="2">
          <div class="grid-content bg-purple">
            <el-row :gutter="20">
              <el-col :span="10">
                <div class="grid-content bg-purple" style="border:0px solid #c8d4e1 ">

                  <el-tabs type="border-card">
                    <el-tab-pane style="height: 650px;">
                      <span slot="label"><i class="el-icon-edit"></i> 文本编辑</span>
                      <el-tabs v-model="activeName" @tab-click="handleClick">
                        <el-tab-pane label="文本" name="text">

                          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px"
                                   class="demo-ruleForm">

                            <el-form-item label-width="0px" prop="desc">
                              <el-input type="textarea" :autosize="{ minRows: 20, maxRows: 25}" placeholder="请输入文本！"
                                        v-model="ruleForm.desc">
                              </el-input>
                            </el-form-item>
                            <el-form-item>
                              <el-button type="primary" @click="submitForm('ruleForm')">生成词云</el-button>
                              <el-button @click="resetForm('ruleForm')">重置</el-button>
                            </el-form-item>
                          </el-form>
                        </el-tab-pane>
                        <el-tab-pane label="自动分词" name="fenci">

                          <el-form :model="ruleForm2" :rules="rules" ref="ruleForm2" label-width="100px"
                                   class="demo-ruleForm">

                            <el-form-item label-width="0px" prop="desc">
                              <el-input type="textarea" :autosize="{ minRows: 20, maxRows: 25}" placeholder="仅供展示分词 以及分词词性！！"
                                        v-model="ruleForm2.desc">
                              </el-input>
                            </el-form-item>
                            <el-form-item>
<!--                              <el-button type="primary" @click="submitForm('ruleForm')">生成词云</el-button>-->
<!--                              <el-button @click="resetForm('ruleForm')">重置</el-button>-->
                            </el-form-item>
                          </el-form>
                        </el-tab-pane>
                        <el-tab-pane label="频数统计" name="third">
                          <el-form :model="ruleForm3" :rules="rules" ref="ruleForm3" label-width="100px"
                                   class="demo-ruleForm">

                            <el-form-item label-width="0px" prop="desc">
                              <el-input type="textarea" :autosize="{ minRows: 20, maxRows: 25}" placeholder="请输入文本！如：
你好,2
小猫,1
小狗,3
"
                                        v-model="ruleForm3.desc">
                              </el-input>
                            </el-form-item>
                            <el-form-item>
                              <el-button type="primary" @click="submitForm3('ruleForm3')">生成词云</el-button>
                              <el-button @click="resetForm('ruleForm3')">重置</el-button>
                            </el-form-item>
                          </el-form>


                        </el-tab-pane>
                      </el-tabs>
                    </el-tab-pane>
                    <el-tab-pane style="height: 650px;">
                      <span slot="label"><i class="el-icon-setting"></i> 效果设置</span>
                      <el-scrollbar height="10px" style="height: 680px; ">
                        <el-form class="qwq" ref="form" :model="form" label-width="80px">
                          <p>背景与边框</p>
                          <el-form-item label="背景颜色:">
                            <el-radio v-model="radio" label="1">透明</el-radio>
                            <el-radio v-model="radio" label='2'>自定义
                              <div class="block">
                                <el-color-picker v-model="color1" style="display: inline;"></el-color-picker>
                              </div>
                            </el-radio>

                          </el-form-item>

                          <el-form-item label="边框设置:">
                            <el-checkbox v-model="checked">显示边框</el-checkbox>
                            <el-input-number v-model="num8" controls-position="right" @change="handleChange"
                                             :size="small">
                            </el-input-number>
                          </el-form-item>

                          <el-form-item label="边框颜色:">
                            <el-radio v-model="radio1" label="1">透明</el-radio>
                            <el-radio v-model="radio1" label="2">自定义

                              <div class="block">
                                <el-color-picker v-model="color3" style="display: inline;"></el-color-picker>
                              </div>
                            </el-radio>

                          </el-form-item>

                          <hr style="border: 1px dashed   #d2cfd4;"/>

                          <p>词性选择</p>
                          <el-form-item label="词性筛选:">
                            <el-select v-model="PartOfSpeech.attribute" style="width: 100px;height: 30px;">
                              <el-option label="默认" value="Default"></el-option>
                              <el-option label="其他" value="Else"></el-option>
                            </el-select>
                          </el-form-item>

                          <hr style="border: 1px dashed   #d2cfd4;;"/>

                          <p>文字方向</p>
                          <el-form-item label="方向设置:">
                            <el-radio v-model="radio2" label="0.9">横竖混排</el-radio>
                            <el-radio v-model="radio2" label="2">仅横向</el-radio>
                            <el-radio v-model="radio2" label="0.1">仅纵向</el-radio>
                          </el-form-item>

                          <hr style="border: 1px dashed   #d2cfd4;;"/>

                          <p>文字间隔</p>
                          <el-form-item label="间隔设置:">
                            <el-radio v-model="radio3" label=2>标准</el-radio>
                            <el-radio v-model="radio3" label=1>紧凑</el-radio>
                            <el-radio v-model="radio3" label=3>较远</el-radio>

                          </el-form-item>

                          <hr style="border: 1px dashed   #d2cfd4;;"/>

                          <p>颜色与字体</p>
                          <el-form-item label="颜色设置:">
                            <el-radio v-model="radio4" label="1">颜色随机</el-radio>

                            <br>
                            <el-radio v-model="radio4" label="2">单种颜色
                              <div class="block">
                                <el-color-picker v-model="color4" style="display: inline;"></el-color-picker>
                              </div>
                            </el-radio>

                            <br>
                            <el-radio v-model="radio4" label="3">预设组合1
                              <div class="block">
                                <el-color-picker v-model="color41" style="display: inline;"></el-color-picker>
                              </div>
                            </el-radio>

                            <br/>
                            <el-radio v-model="radio4" label="4">预设组合2</el-radio>
                            <div class="block" v-model="color42"
                                 style="background-image: linear-gradient(to right, #f5f5f5 , #aeaeae);width: 56px;">
                              <el-color-picker style="display: inline;"></el-color-picker>
                            </div>
                            <br/>
                            <el-radio v-model="radio4" label="5">预设组合3</el-radio>
                            <div class="block" v-model="color43"
                                 style="background-image: linear-gradient(to right, #f5f5f5 , #aeaeae);width: 56px;">
                              <el-color-picker style="display: inline;"></el-color-picker>
                            </div>
                          </el-form-item>

                          <el-form-item label="字体选择:">
                            <el-select v-model="typeface.choosed" style="width: 100px;height: 30px;">
                              <el-option label="微软雅黑 常规" value="msyh.ttc"></el-option>
                              <el-option label="微软雅黑 粗体" value="msyhbd.ttc"></el-option>
                              <el-option label="仿宋" value="simfang.ttf"></el-option>
                              <el-option label="楷体" value="simkai.ttf"></el-option>
                              <el-option label="华文彩云" value="STCAIYUN.TTF"></el-option>
                              <el-option label="繁体" value="msjh.ttc"></el-option>
                              <el-option label="方正舒体" value="FZSTK.TTF"></el-option>
                              <el-option label="英文斜体" value="BRUSHSCI.TTF"></el-option>
                              <el-option label="华文行楷" value="STXINGKA.TTF"></el-option>
                              <el-option label="华文琥珀" value="STHUPO.TTF"></el-option>
                            </el-select>
                            <el-checkbox v-model="checked1" style="margin-left: 3%;">加粗</el-checkbox>

                          </el-form-item>
                          <el-form-item label="字体大小:">
                            <el-checkbox v-model="radio5" label="1" style="border-radius: 50%;">自动</el-checkbox>
                          </el-form-item>

                          <hr style="border: 1px dashed   #d2cfd4;"/>

                          <p>自定义设置</p>
                          <el-table
                            :data="tableData"
                            border
                            style="width: 100%">
                            <el-table-column
                              prop="date"
                              label="分词"
                              width="180">
                            </el-table-column>
                            <el-table-column
                              prop="name"
                              label="大小"
                              width="180">
                              <!--                              <teleport slot-scope="scope">-->
                              <!--                                <el-input-number v-model="scope.row.num" :value="1" controls-position="right"-->
                              <!--                                                 @change="handleChange" :min="1" :max="10"-->
                              <!--                                                 :size="small"></el-input-number>-->
                              <!--                              </teleport>-->
                            </el-table-column>
                            <el-table-column
                              prop="address"
                              label="颜色">
                              <!--                              <teleport slot-scope="scope">-->
                              <!--                                <div class="block">-->
                              <!--                                  <el-color-picker v-model="scope.row" style="display: inline;"></el-color-picker>-->
                              <!--                                </div>-->
                              <!--                              </teleport>-->
                            </el-table-column>
                          </el-table>
                          <el-form-item>
                            <el-button style="margin: 10px" type="primary" @click="submitForm('ruleForm')">以文本生成词云</el-button>
                            <el-button style="margin: 10px" type="primary" @click="submitForm3('ruleForm3')">以词数生成词云</el-button>

                            <!--                          <el-button-->

                            <!--                            @click="onSubmit">生成文字云-->
                            <!--                          </el-button>-->
                          </el-form-item>
                        </el-form>
                      </el-scrollbar>

                      <!--                      <el-scrollbar height="1" style="height: 100%; border: 0px solid #c8d4e1">-->
                      <!--                        <el-form ref="form" :model="form" label-width="80px">-->
                      <!--                          <h5>背景与边框</h5>-->
                      <!--                          <el-form-item label="背景颜色">-->
                      <!--                            <el-radio-group v-model="form.resource">-->

                      <!--                              <el-radio label="透明"></el-radio>-->
                      <!--                              <el-radio label="自定义">-->


                      <!--                                <el-color-picker v-model="color1"></el-color-picker>-->

                      <!--                              </el-radio>-->
                      <!--                            </el-radio-group>-->
                      <!--                          </el-form-item>-->


                      <!--                          <el-form-item label="边框设置">-->
                      <!--                            <el-select v-model="form.region" placeholder="请选择边框大小">-->
                      <!--                              <el-option label="2px" value="shanghai"></el-option>-->
                      <!--                              <el-option label="3px" value="beijing"></el-option>-->
                      <!--                              <el-option label="4px" value="beijing"></el-option>-->
                      <!--                              <el-option label="5px" value="beijing"></el-option>-->
                      <!--                            </el-select>-->
                      <!--                          </el-form-item>-->

                      <!--                          <el-form-item label="边框颜色">-->
                      <!--                            <el-radio-group v-model="form.resource1">-->

                      <!--                              <el-radio label="透明"></el-radio>-->
                      <!--                              <el-radio label="自定义">-->


                      <!--                                <el-color-picker v-model="color1"></el-color-picker>-->

                      <!--                              </el-radio>-->
                      <!--                            </el-radio-group>-->
                      <!--                          </el-form-item>-->

                      <!--                          <hr>-->
                      <!--                          <h5>词性选择</h5>-->

                      <!--                          <el-form-item label="词性选择">-->
                      <!--                            <el-select v-model="form.region" placeholder="请选择词性">-->
                      <!--                              <el-option label="动词" value="shanghai"></el-option>-->
                      <!--                              <el-option label="名词" value="beijing"></el-option>-->

                      <!--                            </el-select>-->
                      <!--                          </el-form-item>-->

                      <!--                          <hr>-->
                      <!--                          <h5>文字方向</h5>-->

                      <!--                          <el-form-item label="方向设置">-->
                      <!--                            <el-radio-group v-model="form.resource">-->
                      <!--                              <el-radio label="仅横向"></el-radio>-->
                      <!--                              <el-radio label="仅纵向"></el-radio>-->
                      <!--                              <el-radio label="横竖混排"></el-radio>-->
                      <!--                            </el-radio-group>-->
                      <!--                          </el-form-item>-->
                      <!--                          <hr>-->
                      <!--                          <h5>文字间隔</h5>-->
                      <!--                          <el-form-item label="间隔设置">-->
                      <!--                            <el-radio-group v-model="form.resource">-->
                      <!--                              <el-radio label="标准"></el-radio>-->
                      <!--                              <el-radio label="紧凑"></el-radio>-->
                      <!--                              <el-radio label="拥挤"></el-radio>-->

                      <!--                            </el-radio-group>-->
                      <!--                          </el-form-item>-->
                      <!--                          <hr>-->
                      <!--                          <h5>颜色与字体</h5>-->

                      <!--                          <el-form-item label="字体颜色">-->
                      <!--                            <el-radio-group v-model="form.resource">-->
                      <!--                              <el-radio label="单一颜色"></el-radio>-->
                      <!--                              <el-radio label="颜色随机"></el-radio>-->
                      <!--                            </el-radio-group>-->
                      <!--                          </el-form-item>-->


                      <!--                          <el-form-item label="字体选择">-->
                      <!--                            <el-select v-model="form.region" placeholder="请选择字体">-->
                      <!--                              <el-option label="字体一" value="shanghai"></el-option>-->
                      <!--                              <el-option label="字体二" value="beijing"></el-option>-->

                      <!--                            </el-select>-->
                      <!--                          </el-form-item>-->

                      <!--                          <hr>-->

                      <!--                          <h5>自定义设置</h5>-->
                      <!--                          xxx-->
                      <!--                          xxx-->
                      <!--                          xxx-->
                      <!--                          <hr>-->

                      <!--                          <el-form-item>-->
                      <!--                            <el-button type="primary" @click="onSubmit">生成词云</el-button>-->
                      <!--                            <el-button>取消</el-button>-->
                      <!--                          </el-form-item>-->
                      <!--                        </el-form>-->


                      <!--                      </el-scrollbar>-->


                    </el-tab-pane>
                    <el-tab-pane style="height: 637px;">
                      <span slot="label"><i class="el-icon-picture-outline"></i>词云形状
                      </span>

                      <p>自定义词云模板:</p>


                      <el-upload
                        class="upload-demo"
                        drag
                        :limit="1"
                        :on-success="handleAvatarSuccess"
                        :on-exceed="handleExceed"
                        :on-remove="removeImg"
                        action="http://119.3.204.138:8000/api/upload/"
                        multiple
                      >
                        <i class="el-icon-upload"></i>
                        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                        <template #tip>
                          <div class="el-upload__tip">
                            只能上传 jpg/png 文件，且不超过 500kb
                          </div>
                        </template>
                      </el-upload>

                      <p>词云模板选择：</p>
                      <el-scrollbar height="10" style="height: 342px; border: 2px solid #c8d4e1">


                        <div class="picture_suo_t" style="display: block;height: 330px;">
                          <div class="picture_suo_img" :class="{'suo-img': sty==index}" @click="onImg(index,value)"
                               v-for="(value,index) in img_list" :key="index">
                            <img class="lazy" :src="'http://119.3.204.138:8000/statics/img_template/'+value">

                          </div>


                        </div>


                      </el-scrollbar>


                    </el-tab-pane>


                  </el-tabs>


                </div>
              </el-col>
              <el-col :span="14">
                <div class="grid-content bg-purple">
                  <el-card class="box-card" style="text-align: center">

                    <template #header>
                      <div class="card-header">
                        <span>文字云效果预览：</span>
                        <div>
                          <el-button type="primary" @click="downloadImg" plain>下载图片<i class=" el-icon-download"></i>
                          </el-button>


                          <el-button type="primary" @click="open" plain>生成链接<i class=" el-icon-share"></i></el-button>
                        </div>

                        <!--      <el-button class="button" type="text">操作按钮</el-button>-->
                      </div>
                    </template>

<template >
                    <div class="photo">


                      <div
                        v-loading="loading"
                        element-loading-text="拼命加载中"
                        element-loading-spinner="el-icon-loading"
                        element-loading-background="rgba(0, 0, 0, 0.8)"
                        :data="img_url"
                        style="width: 100%;height: 100%;">
                        <img style="height: 600px;width: 600px;" :src=img_url alt="">
                      </div>

                      <!--                      <img  v-if="img_jd" style=" padding: 80px; height: 225px;width: 225px;"-->
                      <!--                           src='@/assets/1495.gif'-->

                    </div>
</template>
                  </el-card>


                </div>
              </el-col>
            </el-row>

          </div>
        </el-col>
      </el-row>
    </div>


    <Footer></Footer>


  </div>


</template>

<script>
import Header from './common/Header';
import Banner from "./common/Banner";
import Footer from "./common/Footer";
import loading_img from "../../src/assets/1495.gif"
import Clipboard from 'clipboard';

export default {
  name: "WordCloud",

  data() {
    return {

      checked1: '',      // 字体加粗
      "font": [
        "msyh.ttc",
        "msyhbd.ttc",
        "simfang.ttf",
        "simkai.ttf",
        "STCAIYUN.TTF",
        "msjh.ttc",
        "FZSTK.TTF",
        "BRUSHSCI.TTF",
        "STXINGKA.TTF",
        "STHUPO.TTF"
      ],


      small: '',
      radio: "1",     // 背景颜色是否为透明  1 为透明 2为自定义
      radio1: "1",    // 边框颜色是否为透明  1 为透明 2为自定义
      radio2: "0.9",  // 方向设置 0.9为横竖都有,2 为仅横向 0 仅纵向
      radio3: '2',    // 间隔设置 2为标准 ，1为紧凑 3为较远
      radio4: "1",    // 颜色设置 1为随机
      radio5: true,   // 字体大小

      num8: 1,        // 边框大小
      color1: '#BEBEBE',  // 背景颜色
      color3: "#BEBEBE",  // 边框颜色
      color4: '#BEBEBE',
      color41:'#BEBEBE',
      color42: '#BEBEBE',
      color43: '#BEBEBE',
      color2: "linear-gradient(#e66465, #9198e5)",
      checked: false,     // 是否显示边框
      PartOfSpeech: {
        attribute: 'Default',
      },
      typeface: {
        choosed: "simkai.ttf",

      },
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      tableData: [{
        date: '分词1文本',
        name: '王小虎',
        address: ''
      }, {
        date: '分词2文本',
        name: '王小虎',
        address: ''
      }, {
        date: '分词3文本',
        name: '王小虎',
        address: ''
      }],


      loading: false,

      //需要下载的词云图片名
      ciyun_img: '92F687CCB6E211EB80695F79F28AFEE0.png',

      // 需要模板图片生成词云的 模板图片名
      img_name: '11.png',

      // 用户自定义模板图片生成词云的 模板图片名
      user_img_name: '',

      // 默认加载图片
      img_url: `${this.$settings.Host}`+'/statics/img_ciyun/3C5961A4B6C011EB80695F79F28AFEE0.png',

      // 模板图片的索引
      sty: 'None',

      // 模板图片地址的列表
      img_list: '',

      // 文本编辑下的自动分词表单内容
      ruleForm2: {
        desc: '',
      },
      // 文本编辑下的频数统计表单内容
      ruleForm3: {
        desc: '',
      },
      ruleForm: {
        desc: "立信(重庆)市场研究股份有限公司于2001年3月成立，是中国西部地区规模最大的市场研究机构；中国信息协会市场研究分会副会长单位、常务理事单位。2005年1月荣获国家统计局民间涉外调查管理处颁发的《涉外调查许可证》，具备从事涉外调查的资格。2012年4月成功通过ISO20252：2006第三方认证审核，2015年6月再次审核通过，是中国西部首家通过国际标准认证的公司。\n" +
          "   立信公司自成立以来，始终坚持专业、规范的项目执行为重点发展方向，分公司遍布贵州、甘肃、青海、宁夏、云南、四川等多个省份。通过多年的发展，立信公司拥有一流的硬件设施，最优秀的督导和项目管理人员，完善的项目管理体系，强大的管理平台和不断创新的调研技术。目前立信公司全职人员已达200人以上，65个城市实地执行能力，50万人次以上的年访问量。多年来，在完善执行网络基础上持续发展产品链，已逐步形成立信的核心竞争力。\n" +
          "   2011年，成立西部地区最大的呼叫中心，拥有坐席168个。2013年，立信联合全国市场研究知名企业共同打造中国最大的网络调查平台——调研吧，为行业提供公共的数据采集平台。\n" +
          "   目前，立信已成为中国唯一 一家全渠道（传统、CATI、网络）数据采集公司。立信人将通过不懈努力，立志打造全国最大的数据采集公司，成为中国数据采集第一品牌。",
      },

      // error 模块
      rules: {
        desc: [
          {required: true, message: '请填写文本！', trigger: 'blur'}
        ]
      },
      activeName: 'text',

    };

  },
  created() {
    // 获取模板图片
    this.$axios.post(`${this.$settings.Host}/api/template/`, {})
      .then((res) => {
        // alert(res.data.data.img_list)
        this.img_list = res.data.data.img_list
      })
      .catch((error) => {
        this.$message.error(error.response.data.msg);
      })

  },

  methods: {
    handleChange(value) {
      console.log(value);
    },


    // 复制链接
    copy(data) {
      let url = data
      let oInput = document.createElement('input')
      oInput.value = url
      document.body.appendChild(oInput)
      oInput.select() // 选择对象
      document.execCommand("Copy") // 执行浏览器复制命令

      oInput.remove()
    },
    open() {
      this.$confirm(<p>链接：<a href={this.img_url} style="text-decoration:none; color:#2440B3">{this.img_url}</a>
      </p>, '生成连接', {
        confirmButtonText: '复制',
        cancelButtonText: '取消',
        // center: true,


        dangerouslyUseHTMLString: true,
        customClass: 'myClass',

      }).then(() => {


        this.copy(this.img_url)

        this.$message({
          type: 'success',
          message: '复制成功!',
        });


      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消复制'
        });
      });
    },


    // 下载图片
    downloadImg() {
      var elemIF = document.createElement('iframe')
      elemIF.src = `${this.$settings.Host}/api/download/` + this.ciyun_img
      elemIF.style.display = 'none'
      document.body.appendChild(elemIF)

    },


    // 文件上传
    handleAvatarSuccess(res) {
      // alert(res.data.data.img_name)
      this.$message({
        message: '上传成功！，快去生成词云吧！',
        type: 'success'
      });
      this.user_img_name = res.data.img_name
    },
    removeImg() {
      this.user_img_name = ''
      this.$message('已取消自定义模板选择了呢');
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },


    // 模板选择
    onImg(index, value) {

      if (this.sty == index) {
        this.sty = 'None'
        this.$message('已取消模板选择了呢');
        this.img_name = '11.png'

      } else {
        this.sty = index
        this.$message({
          message: '选择成功，会优先选择自定义模板呢，需要词云模板记得取消自定义模板呢！快去生成词云吧！' + value,
          type: 'success'
        });
        this.img_name = value
      }


    },

    onSubmit2() {
      alert(this.radio, this.color1)


      console.log('submit!');
    },
    onSubmit1() {


      if (this.radio == 2) {
        // alert(this.radio)
        alert('背景颜色' + this.color1)
      } else {
        alert('无背景颜色' + this.radio)
      }
      if (this.checked === true) {
        // alert(this.checked)
        alert('有边框' + this.num8 + '边框颜色' + this.color3)
      } else {
        alert('无有边框' + this.checked)
      }
      alert('方向显示' + this.radio2)
      alert('间隔设置' + this.radio3)
      alert('字体' + this.typeface.choosed)


      console.log('submit!');
    },
    handleClick1(tab, event) {
      // console.log(tab, event, 'qwq');
    },
    handleClick(tab, event) {
      // console.log(tab, event, 'qwq1');
    },


    // 文本编辑下的文本 生成图片，点击所触发的事件
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {

          if (this.ruleForm.desc.length < 1) {
            this.$message({
              showClose: true,
              message: '文本不能为空呢！',
              type: 'error'
            });
          } else {

            // 选择透明 清除自定义颜色 改为1 发给后端判断为透明
            if (this.radio == '1') {
              this.color1 = '0'
            }
            if (this.checked == false) {
              this.color3 = '0';
              this.num8 = '0';
            }
            if (this.radio4 === '1') {
              this.color4 = '0'

            }


            this.loading = true

            // 发送axios请求 生成图片链接
            this.$axios.post(`${this.$settings.Host}/api/ciyun/`, {
              "data_text": this.ruleForm.desc,
              "b_color": this.color1,
              "contour_width": this.num8,
              "contour_color": this.color3,
              "margin": this.radio3,
              "font_str": this.typeface.choosed,
              "img_name": this.img_name,
              "user_img_name": this.user_img_name,
              "prefer_horizontal": this.radio2,
              "byte_color": this.color4,

            })
              .then((res) => {


                this.ciyun_img = res.data.data.photo_url
                this.img_url = this.$settings.Host + '/statics/img_ciyun/' + res.data.data.photo_url
                // alert(this.img_url)
                this.loading = false
                this.ruleForm3.desc = res.data.data.str_a
                var a = res.data.data.data_text_list
                let txt = ''
                for (let i in a) {
                  // console.log(i, ' => ', a[i])
                  txt = txt + a[i] + '\n'
                }
                // alert(txt)
                this.ruleForm2.desc = txt


                this.data_list = res.data;
                // alert(res.data)
              })
              .catch((error) => {
                alert(error + 'sdadsadsa')
              })

            // alert(this.ruleForm.desc);

          }

        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },

    // 文本编辑下的频数统计 生成图片，点击所触发的事件
    submitForm3(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {

          if (this.ruleForm3.desc.length < 1) {
            alert('qwq')

            this.$message({
              showClose: true,
              message: '文本不能为空呢！',
              type: 'error'
            });


          } else {

            // 选择透明 清除自定义颜色 改为1 发给后端判断为透明
            if (this.radio == '1') {
              this.color1 = '0'
            }
            if (this.checked == false) {
              this.color3 = '0';
              this.num8 = '0';
            }
            if (this.radio4 === '1') {
              this.color4 = '0'

            }


            this.loading = true
            // 发送axios请求 生成图片链接
            this.$axios.post(`${this.$settings.Host}/api/update/`, {
              "data_text": this.ruleForm3.desc,
              "b_color": this.color1,
              "contour_width": this.num8,
              "contour_color": this.color3,
              "margin": this.radio3,
              "font_str": this.typeface.choosed,
              "img_name": this.img_name,
              "user_img_name": this.user_img_name,
              "prefer_horizontal": this.radio2,
              "byte_color": this.color4,

            })
              .then((res) => {
                this.img_url = this.$settings.Host + '/statics/img_ciyun/' + res.data.data.photo_url
                this.ciyun_img = res.data.data.photo_url
                // this.img_url = this.$settings.Host + '/' + res.data.data.photo_url
                // alert(this.img_url)
                this.loading = false
                // this.ruleForm3.desc = res.data.data.str_a
                var a = res.data.data.data_text_list
                let txt = ''
                // 换行显示
                for (let i in a) {
                  // console.log(i, ' => ', a[i])
                  txt = txt + a[i] + '\n'
                }
                // alert(txt)
                this.ruleForm2.desc = txt

                this.data_list = res.data;
                // alert(res.data)
              })
              .catch((error) => {
                alert(error + 'qqqqqqq')
              })

            // alert(this.ruleForm.desc);

          }

        } else {
          console.log('error submit!!');
                  this.$message({
              showClose: true,
              message: '频数统计文本不能为空呢！',
              type: 'error'
            });
          return false;
        }
      });
    },

    // 内容重置
    resetForm(formName) {
      this.ruleForm.desc = '';
    }

  },


  components: {
    Header,
    Banner,
    Footer

  }

}
</script>

<style scoped>


.qwq p {
  width: 100px;
  height: 1.5625rem;
  padding-left: 3%;
  border-style: solid;
  border-left-color: #0000FF;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
}



.block {
  display: inline;
  line-height: 43px;

}

/* 	.el-input-number  {
  width: 100px;
  height: 32px;
  } */


.el-input--suffix .el-input__inner {
  padding-right: 30px;
  height: 30px;
}

.el-color-picker__color {
  border: none;
}

/*.el-icon-close:before {*/
/*  display: none;*/
/*  content: "\e6db";*/
/*}*/

.el-page-header__title {
  font-size: 12px;
  font-weight: 500;
}

/* 	.el-input__inner{
  height:30px;
  } */
.el-input__icon {
  line-height: 30px;
}

/*.el-button--primary {*/
/*  color: #FFF;*/
/*  background-color: #2a5fc7;*/
/*  !*border-color: #4;*!*/
/*  height: 30px;*/
/*  line-height: 30px;*/
/*}*/

/*.el-button {*/
/*  display: inline-block;*/
/*  line-height: 0;*/
/*  height: 30px;*/
/*}*/

.el-table td, .el-table th.is-leaf {
  border-bottom: 1px solid #EBEEF5;
  margin: 0;
  padding: 0;
}

.el-table thead {
  color: #65676b;
  /* font-weight: 500; */
  font-weight: normal;
  height: 30px;
  line-height: 30px;
  font-size: 12px;
}

.el-table .cell, .el-table--border td:first-child .cell, .el-table--border th:first-child .cell {
  /* padding-left: 10px; */
  text-align: center;
  font-size: 10px;
}

.el-table .cell {
  margin: 0;
  padding: 0;
}

.el-table--border th {
  background-color: #e4e4e4;
}

.el-form-item {
  white-space: nowrap;
}

/* .el-checkbox__inner{
   border-radius: 50%;
 } */


.myClass {

  width: 600px;
}

.lazy {
  height: 100px;
  width: 100px;


}

.picture_suo_t {
  margin: 0;
  padding: 30px;
  height: 300px;
  display: block;
}

.picture_suo_img.suo-img {
  padding: 0;
  width: 100px;
  height: 100px;
  margin: 5px 30px;
  float: left;
  cursor: pointer;
  border: 3px solid #c8d4e1;
}

.picture_suo_img {

  padding: 0;
  width: 100px;
  height: 100px;
  margin: 6px 30px;
  border: 2px solid #e4e4e4;
  float: left;
  cursor: pointer;
}


.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 100%;
}


.photo_download a {
  text-decoration: none;
  color: black;
}

.photo {
  /*height: 600px;*/
  width: 78%;
  /*margin-bottom: 5px;*/
  background-color: #e5e9f2;
  margin-left: 11%;
  text-align: center;
  align-items: center;


}

.wordcloud {
  margin-top: 10px;

}


.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: red;
}

.bg-purple {
  background: #eeeeef;
  /*
  rgba(255, 255, 255, 0.9)
   */
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}


</style>
