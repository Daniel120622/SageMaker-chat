<h1 align="center">Bedrock Chat (BrChat)</h1>

<p align="center">
  <img src="https://img.shields.io/github/v/release/aws-samples/bedrock-chat?style=flat-square" />
  <img src="https://img.shields.io/github/license/aws-samples/bedrock-chat?style=flat-square" />
  <img src="https://img.shields.io/github/actions/workflow/status/aws-samples/bedrock-chat/cdk.yml?style=flat-square" />
  <a href="https://github.com/aws-samples/bedrock-chat/issues?q=is%3Aissue%20state%3Aopen%20label%3Aroadmap">
    <img src="https://img.shields.io/badge/roadmap-view-blue?style=flat-square" />
  </a>
</p>

[English](https://github.com/aws-samples/bedrock-chat/blob/v3/README.md) | [日本語](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_ja-JP.md) | [한국어](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_ko-KR.md) | [中文](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_zh-CN.md) | [Français](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_fr-FR.md) | [Deutsch](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_de-DE.md) | [Español](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_es-ES.md) | [Italian](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_it-IT.md) | [Norsk](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_nb-NO.md) | [ไทย](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_th-TH.md) | [Bahasa Indonesia](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_id-ID.md) | [Bahasa Melayu](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_ms-MY.md) | [Tiếng Việt](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_vi-VN.md) | [Polski](https://github.com/aws-samples/bedrock-chat/blob/v3/docs/README_pl-PL.md)

แพลตฟอร์มปัญญาประดิษฐ์เชิงสร้างสรรค์แบบหลายภาษาที่ขับเคลื่อนด้วย [Amazon Bedrock](https://aws.amazon.com/bedrock/)
รองรับการแชท บอทที่กำหนดเองพร้อมความรู้ (RAG) การแบ่งปันบอทผ่านร้านค้าบอท และการทำงานอัตโนมัติของงานโดยใช้เอเจนต์

![](./imgs/demo.gif)

> [!คำเตือน]
>
> **เปิดตัว V3 แล้ว กรุณาตรวจสอบคู่มือการย้ายระบบ [migration guide](./migration/V2_TO_V3_th-TH.md) อย่างระมัดระวัง** หากไม่ระมัดระวัง **บอทจาก V2 จะใช้งานไม่ได้**

### การปรับแต่งบอท / ร้านค้าบอท

เพิ่มคำแนะนำและความรู้ของคุณเอง (หรือที่เรียกว่า [RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/)) บอทสามารถแบ่งปันระหว่างผู้ใช้แอปพลิเคชันผ่านร้านค้าบอท บอทที่กำหนดเองยังสามารถเผยแพร่เป็น API แบบสแตนด์อโลนได้ (ดูรายละเอียด[ที่นี่](./PUBLISH_API_th-TH.md))

<details>
<summary>ภาพหน้าจอ</summary>

![](./imgs/customized_bot_creation.png)
![](./imgs/fine_grained_permission.png)
![](./imgs/bot_store.png)
![](./imgs/bot_api_publish_screenshot3.png)

คุณยังสามารถนำเข้า [Amazon Bedrock's KnowledgeBase](https://aws.amazon.com/bedrock/knowledge-bases/) ที่มีอยู่

![](./imgs/import_existing_kb.png)

</details>

> [!สำคัญ]
> ด้วยเหตุผลด้านการกำกับดูแล เฉพาะผู้ใช้ที่ได้รับอนุญาตเท่านั้นที่สามารถสร้างบอทที่กำหนดเองได้ เพื่ออนุญาตให้สร้างบอทที่กำหนดเอง ผู้ใช้ต้องเป็นสมาชิกของกลุ่มที่เรียกว่า `CreatingBotAllowed` ซึ่งสามารถตั้งค่าได้ผ่านคอนโซลการจัดการ > Amazon Cognito User pools หรือ aws cli โปรดทราบว่าสามารถอ้างอิง user pool id ได้โดยเข้าถึง CloudFormation > BedrockChatStack > Outputs > `AuthUserPoolIdxxxx`

### คุณสมบัติการดูแลระบบ

การจัดการ API การทำเครื่องหมายบอทเป็นสิ่งสำคัญ วิเคราะห์การใช้งานสำหรับบอท [รายละเอียด](./ADMINISTRATOR_th-TH.md)

<details>
<summary>ภาพหน้าจอ</summary>

![](./imgs/admin_bot_menue.png)
![](./imgs/bot_store.png)
![](./imgs/admn_api_management.png)
![](./imgs/admin_bot_analytics.png))

</details>

### เอเจนต์

โดยใช้ [ฟังก์ชันเอเจนต์](./AGENT_th-TH.md) แชทบอทของคุณสามารถจัดการงานที่ซับซ้อนได้โดยอัตโนมัติ ตัวอย่างเช่น เพื่อตอบคำถามของผู้ใช้ เอเจนต์สามารถดึงข้อมูลที่จำเป็นจากเครื่องมือภายนอกหรือแบ่งงานออกเป็นหลายขั้นตอนเพื่อประมวลผล

<details>
<summary>ภาพหน้าจอ</summary>

![](./imgs/agent1.png)
![](./imgs/agent2.png)

</details>

## 🚀 การปรับใช้งานแบบง่ายมาก

- ในภูมิภาค us-east-1 เปิด [การเข้าถึงโมเดล Bedrock](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/modelaccess) > `จัดการการเข้าถึงโมเดล` > เลือกโมเดลทั้งหมดที่คุณต้องการใช้ แล้วกด `บันทึกการเปลี่ยนแปลง`

<details>
<summary>ภาพหน้าจอ</summary>

![](./imgs/model_screenshot.png)

</details>

- เปิด [CloudShell](https://console.aws.amazon.com/cloudshell/home) ในภูมิภาคที่คุณต้องการปรับใช้งาน
- เรียกใช้การปรับใช้งานด้วยคำสั่งต่อไปนี้ หากคุณต้องการระบุเวอร์ชันที่จะปรับใช้งานหรือต้องการใช้นโยบายความปลอดภัย กรุณาระบุพารามิเตอร์ที่เหมาะสมจาก [พารามิเตอร์เสริม](#พารามิเตอร์เสริม)

```sh
git clone https://github.com/aws-samples/bedrock-chat.git
cd bedrock-chat
chmod +x bin.sh
./bin.sh
```

- คุณจะได้รับการถามว่าเป็นผู้ใช้ใหม่หรือใช้ v3 หากคุณไม่ใช่ผู้ใช้ต่อเนื่องจาก v0 กรุณากรอก `y`

### พารามิเตอร์เสริม

คุณสามารถระบุพารามิเตอร์ต่อไปนี้ระหว่างการปรับใช้งานเพื่อเพิ่มความปลอดภัยและการปรับแต่ง:

- **--disable-self-register**: ปิดการลงทะเบียนด้วยตนเอง (ค่าเริ่มต้น: เปิด) หากตั้งค่านี้ คุณจะต้องสร้างผู้ใช้ทั้งหมดบน Cognito และจะไม่อนุญาตให้ผู้ใช้ลงทะเบียนบัญชีด้วยตนเอง
- **--enable-lambda-snapstart**: เปิดใช้งาน [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) (ค่าเริ่มต้น: ปิด) หากตั้งค่านี้ จะปรับปรุงเวลาเริ่มต้นแบบเย็นสำหรับฟังก์ชัน Lambda โดยให้เวลาตอบสนองที่เร็วขึ้นเพื่อประสบการณ์ผู้ใช้ที่ดีขึ้น
- **--ipv4-ranges**: รายการช่วง IPv4 ที่อนุญาตแบบคั่นด้วยเครื่องหมายจุลภาค (ค่าเริ่มต้น: อนุญาต IPv4 ทั้งหมด)
- **--ipv6-ranges**: รายการช่วง IPv6 ที่อนุญาตแบบคั่นด้วยเครื่องหมายจุลภาค (ค่าเริ่มต้น: อนุญาต IPv6 ทั้งหมด)
- **--disable-ipv6**: ปิดการเชื่อมต่อผ่าน IPv6 (ค่าเริ่มต้น: เปิด)
- **--allowed-signup-email-domains**: รายการโดเมนอีเมลที่อนุญาตสำหรับการลงทะเบียนแบบคั่นด้วยเครื่องหมายจุลภาค (ค่าเริ่มต้น: ไม่มีข้อจำกัดโดเมน)
- **--bedrock-region**: กำหนดภูมิภาคที่ Bedrock พร้อมใช้งาน (ค่าเริ่มต้น: us-east-1)
- **--repo-url**: ที่เก็บ Bedrock Chat แบบกำหนดเองเพื่อปรับใช้งาน หากทำการ fork หรือใช้การควบคุมแหล่งที่มาแบบกำหนดเอง (ค่าเริ่มต้น: https://github.com/aws-samples/bedrock-chat.git)
- **--version**: เวอร์ชันของ Bedrock Chat ที่จะปรับใช้งาน (ค่าเริ่มต้น: เวอร์ชันล่าสุดในการพัฒนา)
- **--cdk-json-override**: คุณสามารถแทนที่ค่าคอนเท็กซ์ของ CDK ใดๆ ระหว่างการปรับใช้งานโดยใช้บล็อก JSON แทนที่ ซึ่งช่วยให้คุณสามารถแก้ไขการกำหนดค่าโดยไม่ต้องแก้ไขไฟล์ cdk.json โดยตรง

ตัวอย่างการใช้งาน:

```bash
./bin.sh --cdk-json-override '{
  "context": {
    "selfSignUpEnabled": false,
    "enableLambdaSnapStart": true,
    "allowedIpV4AddressRanges": ["192.168.1.0/24"],
    "allowedSignUpEmailDomains": ["example.com"]
  }
}'
```

JSON แทนที่ต้องมีโครงสร้างเดียวกับ cdk.json คุณสามารถแทนที่ค่าคอนเท็กซ์ใดๆ รวมถึง:

- `selfSignUpEnabled`
- `enableLambdaSnapStart`
- `allowedIpV4AddressRanges`
- `allowedIpV6AddressRanges`
- `allowedSignUpEmailDomains`
- `bedrockRegion`
- `enableRagReplicas`
- `enableBedrockCrossRegionInference`
- และค่าคอนเท็กซ์อื่นๆ ที่กำหนดใน cdk.json

> [!หมายเหตุ]
> ค่าแทนที่จะถูกรวมกับการกำหนดค่า cdk.json ที่มีอยู่ระหว่างการปรับใช้งานใน AWS code build ค่าที่ระบุในการแทนที่จะมีความสำคัญเหนือกว่าค่าใน cdk.json

#### ตัวอย่างคำสั่งพร้อมพารามิเตอร์:

```sh
./bin.sh --disable-self-register --ipv4-ranges "192.0.2.0/25,192.0.2.128/25" --ipv6-ranges "2001:db8:1:2::/64,2001:db8:1:3::/64" --allowed-signup-email-domains "example.com,anotherexample.com" --bedrock-region "us-west-2" --version "v1.2.6"
```

- หลังจากประมาณ 35 นาที คุณจะได้รับผลลัพธ์ต่อไปนี้ ซึ่งคุณสามารถเข้าถึงได้จากเบราว์เซอร์ของคุณ

```
Frontend URL: https://xxxxxxxxx.cloudfront.net
```

![](./imgs/signin.png)

หน้าจอลงทะเบียนจะปรากฏขึ้นดังที่แสดงข้างต้น ที่ซึ่งคุณสามารถลงทะเบียนอีเมลและเข้าสู่ระบบได้

> [!สำคัญ]
> โดยไม่มีการตั้งค่าพารามิเตอร์เสริม วิธีการปรับใช้งานนี้จะอนุญาตให้ทุกคนที่ทราบ URL สามารถลงทะเบียนได้ สำหรับการใช้งานในระบบผลิต แนะนำอย่างยิ่งให้เพิ่มข้อจำกัด IP และปิดการลงทะเบียนด้วยตนเองเพื่อลดความเสี่ยงด้านความปลอดภัย (คุณสามารถกำหนด allowed-signup-email-domains เพื่อจำกัดผู้ใช้ให้เป็นเพียงที่อยู่อีเมลจากโดเมนของบริษัทคุณเท่านั้น) ใช้ทั้ง ipv4-ranges และ ipv6-ranges สำหรับข้อจำกัด IP และปิดการลงทะเบียนด้วยตนเองโดยใช้ disable-self-register เมื่อดำเนินการ ./bin

> [!เคล็ดลับ]
> หาก `Frontend URL` ไม่ปรากฏหรือ Bedrock Chat ไม่ทำงานอย่างถูกต้อง อาจเป็นปัญหากับเวอร์ชันล่าสุด ในกรณีนี้ กรุณาเพิ่ม `--version "v3.0.0"` ไปยังพารามิเตอร์และลองปรับใช้งานอีกครั้ง

## สถาปัตยกรรม

เป็นสถาปัตยกรรมที่สร้างบน AWS managed services โดยไม่ต้องจัดการโครงสร้างพื้นฐาน การใช้ Amazon Bedrock ช่วยให้ไม่ต้องสื่อสารกับ API นอก AWS ซึ่งช่วยให้สามารถปรับใช้แอปพลิเคชันที่มีความสามารถในการขยายขนาด เชื่อถือได้ และปลอดภัย

- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/): ฐานข้อมูล NoSQL สำหรับจัดเก็บประวัติการสนทนา
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) + [AWS Lambda](https://aws.amazon.com/lambda/): จุดสิ้นสุด API แบ็กเอนด์ ([AWS Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter), [FastAPI](https://fastapi.tiangolo.com/))
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) + [S3](https://aws.amazon.com/s3/): การส่งมอบแอปพลิเคชันหน้าบ้าน ([React](https://react.dev/), [Tailwind CSS](https://tailwindcss.com/))
- [AWS WAF](https://aws.amazon.com/waf/): การจำกัดที่อยู่ IP
- [Amazon Cognito](https://aws.amazon.com/cognito/): การรับรองตัวตนผู้ใช้
- [Amazon Bedrock](https://aws.amazon.com/bedrock/): บริการที่จัดการเพื่อใช้โมเดลพื้นฐานผ่าน API
- [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/): ให้อินเทอร์เฟซการจัดการสำหรับ Retrieval-Augmented Generation ([RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/)) พร้อมบริการสำหรับการฝังและแยกวิเคราะห์เอกสาร
- [Amazon EventBridge Pipes](https://aws.amazon.com/eventbridge/pipes/): รับเหตุการณ์จาก DynamoDB stream และเรียกใช้ Step Functions เพื่อฝังความรู้ภายนอก
- [AWS Step Functions](https://aws.amazon.com/step-functions/): จัดการกระบวนการรับข้อมูลเพื่อฝังความรู้ภายนอกลงใน Bedrock Knowledge Bases
- [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/): ทำหน้าที่เป็นฐานข้อมูลแบ็กเอนด์สำหรับ Bedrock Knowledge Bases โดยให้ความสามารถในการค้นหาแบบเต็มข้อความและการค้นหาแบบเวกเตอร์ ช่วยให้สามารถค้นคืนข้อมูลที่เกี่ยวข้องได้อย่างแม่นยำ
- [Amazon Athena](https://aws.amazon.com/athena/): บริการสอบถามเพื่อวิเคราะห์ S3 bucket

![](./imgs/arch.png)

## การปรับใช้งานด้วย CDK

การปรับใช้งานที่ง่ายมากใช้ [AWS CodeBuild](https://aws.amazon.com/codebuild/) เพื่อดำเนินการปรับใช้งานด้วย CDK ภายใน ส่วนนี้จะอธิบายขั้นตอนการปรับใช้งานโดยตรงด้วย CDK

- กรุณามี UNIX, Docker และสภาพแวดล้อมการทำงาน Node.js หากไม่มี คุณสามารถใช้ [Cloud9](https://github.com/aws-samples/cloud9-setup-for-prototyping)

> [!สำคัญ]
> หากพื้นที่จัดเก็บข้อมูลในสภาพแวดล้อมภายในเครื่องไม่เพียงพอระหว่างการปรับใช้งาน CDK bootstrapping อาจส่งผลให้เกิดข้อผิดพลาด หากคุณกำลังทำงานใน Cloud9 เป็นต้น เราแนะนำให้ขยายขนาดพื้นที่ของอินสแตนซ์ก่อนการปรับใช้งาน

- โคลนที่เก็บโค้ดนี้

```
git clone https://github.com/aws-samples/bedrock-chat
```

- ติดตั้งแพ็คเกจ npm

```
cd bedrock-chat
cd cdk
npm ci
```

- หากจำเป็น ให้แก้ไขรายการต่อไปนี้ใน [cdk.json](./cdk/cdk.json) หากจำเป็น

  - `bedrockRegion`: ภูมิภาคที่ Bedrock ใช้งานได้ **หมายเหตุ: Bedrock ยังไม่รองรับทุกภูมิภาค**
  - `allowedIpV4AddressRanges`, `allowedIpV6AddressRanges`: ช่วง IP Address ที่อนุญาต
  - `enableLambdaSnapStart`: ค่าเริ่มต้นคือ true ตั้งค่าเป็น false หากปรับใช้งานในภูมิภาคที่ไม่รองรับ Lambda SnapStart สำหรับฟังก์ชัน Python

- ก่อนปรับใช้งาน CDK คุณจำเป็นต้องทำ Bootstrap หนึ่งครั้งสำหรับภูมิภาคที่คุณกำลังปรับใช้งาน

```
npx cdk bootstrap
```

- ปรับใช้งานโครงการตัวอย่างนี้

```
npx cdk deploy --require-approval never --all
```

- คุณจะได้รับเอาต์พุตที่คล้ายกับด้านล่าง URL ของเว็บแอปพลิเคชันจะแสดงใน `BedrockChatStack.FrontendURL` กรุณาเข้าถึงจากเบราว์เซอร์ของคุณ

```sh
 ✅  BedrockChatStack

✨  Deployment time: 78.57s

Outputs:
BedrockChatStack.AuthUserPoolClientIdXXXXX = xxxxxxx
BedrockChatStack.AuthUserPoolIdXXXXXX = ap-northeast-1_XXXX
BedrockChatStack.BackendApiBackendApiUrlXXXXX = https://xxxxx.execute-api.ap-northeast-1.amazonaws.com
BedrockChatStack.FrontendURL = https://xxxxx.cloudfront.net
```

### กำหนดพารามิเตอร์

คุณสามารถกำหนดพารามิเตอร์สำหรับการปรับใช้งานได้สองวิธี: การใช้ `cdk.json` หรือการใช้ไฟล์ `parameter.ts` ที่ตรวจสอบชนิดได้

#### การใช้ cdk.json (วิธีดั้งเดิม)

วิธีดั้งเดิมในการกำหนดค่าพารามิเตอร์คือการแก้ไขไฟล์ `cdk.json` วิธีนี้เรียบง่ายแต่ขาดการตรวจสอบชนิด:

```json
{
  "app": "npx ts-node --prefer-ts-exts bin/bedrock-chat.ts",
  "context": {
    "bedrockRegion": "us-east-1",
    "allowedIpV4AddressRanges": ["0.0.0.0/1", "128.0.0.0/1"],
    "selfSignUpEnabled": true
  }
}
```

#### การใช้ parameter.ts (วิธีที่แนะนำสำหรับการตรวจสอบชนิด)

สำหรับการตรวจสอบชนิดและประสบการณ์การพัฒนาที่ดีขึ้น คุณสามารถใช้ไฟล์ `parameter.ts` เพื่อกำหนดพารามิเตอร์ของคุณ:

```typescript
// กำหนดพารามิเตอร์สำหรับสภาพแวดล้อมเริ่มต้น
bedrockChatParams.set("default", {
  bedrockRegion: "us-east-1",
  allowedIpV4AddressRanges: ["192.168.0.0/16"],
  selfSignUpEnabled: true,
});

// กำหนดพารามิเตอร์สำหรับสภาพแวดล้อมเพิ่มเติม
bedrockChatParams.set("dev", {
  bedrockRegion: "us-west-2",
  allowedIpV4AddressRanges: ["10.0.0.0/8"],
  enableRagReplicas: false, // ประหยัดค่าใช้จ่ายสำหรับสภาพแวดล้อม dev
});

bedrockChatParams.set("prod", {
  bedrockRegion: "us-east-1",
  allowedIpV4AddressRanges: ["172.16.0.0/12"],
  enableLambdaSnapStart: true,
  enableRagReplicas: true, // ความพร้อมใช้งานที่เพิ่มขึ้นสำหรับการผลิต
});
```

> [!หมายเหตุ]
> ผู้ใช้ปัจจุบันสามารถใช้ `cdk.json` ต่อไปโดยไม่มีการเปลี่ยนแปลง วิธีการใน `parameter.ts` แนะนำสำหรับการปรับใช้งานใหม่หรือเมื่อคุณต้องจัดการหลายสภาพแวดล้อม

### การปรับใช้งานหลายสภาพแวดล้อม

คุณสามารถปรับใช้งานหลายสภาพแวดล้อมจากโค้ดเดียวกันโดยใช้ไฟล์ `parameter.ts` และตัวเลือก `-c envName`

#### ข้อกำหนดเบื้องต้น

1. กำหนดสภาพแวดล้อมของคุณใน `parameter.ts` ตามที่แสดงข้างต้น
2. แต่ละสภาพแวดล้อมจะมีทรัพยากรของตนเองพร้อมคำนำหน้าเฉพาะสภาพแวดล้อม

#### คำสั่งปรับใช้งาน

เพื่อปรับใช้งานสภาพแวดล้อมเฉพาะ:

```bash
# ปรับใช้งานสภาพแวดล้อม dev
npx cdk deploy --all -c envName=dev

# ปรับใช้งานสภาพแวดล้อม prod
npx cdk deploy --all -c envName=prod
```

หากไม่มีการระบุสภาพแวดล้อม สภาพแวดล้อม "default" จะถูกใช้:

```bash
# ปรับใช้งานสภาพแวดล้อมเริ่มต้น
npx cdk deploy --all
```

#### หมายเหตุสำคัญ

1. **การตั้งชื่อสแต็ก**:

   - สแต็กหลักสำหรับแต่ละสภาพแวดล้อมจะมีคำนำหน้าด้วยชื่อสภาพแวดล้อม (เช่น `dev-BedrockChatStack`, `prod-BedrockChatStack`)
   - อย่างไรก็ตาม สแต็กบอทแบบกำหนดเองเช่น (`BrChatKbStack*`) และสแต็กการเผยแพร่ API (`ApiPublishmentStack*`) จะไม่ได้รับคำนำหน้าสภาพแวดล้อมเนื่องจากถูกสร้างแบบไดนามิกในระหว่างการรันไทม์

2. **การตั้งชื่อทรัพยากร**:

   - เพียงบางทรัพยากรเท่านั้นที่ได้รับคำนำหน้าสภาพแวดล้อมในชื่อของพวกเขา (เช่น ตาราง `dev_ddb_export`, `dev-FrontendWebAcl`)
   - ทรัพยากรส่วนใหญ่คงชื่อเดิมแต่แยกกันโดยอยู่ในสแต็กที่แตกต่างกัน

3. **การระบุสภาพแวดล้อม**:

   - ทรัพยากรทั้งหมดจะมีแท็ก `CDKEnvironment` ที่มีชื่อสภาพแวดล้อม
   - คุณสามารถใช้แท็กนี้เพื่อระบุว่าทรัพยากรใดอยู่ในสภาพแวดล้อมใด
   - ตัวอย่าง: `CDKEnvironment: dev` หรือ `CDKEnvironment: prod`

4. **การแทนที่สภาพแวดล้อมเริ่มต้น**: หากคุณกำหนดสภาพแวดล้อม "default" ใน `parameter.ts` จะแทนที่การตั้งค่าใน `cdk.json` เพื่อใช้ `cdk.json` ต่อไป ไม่ต้องกำหนดสภาพแวดล้อม "default" ใน `parameter.ts`

5. **ข้อกำหนดสภาพแวดล้อม**: เพื่อสร้างสภาพแวดล้อมนอกเหนือจาก "default" คุณต้องใช้ `parameter.ts` ตัวเลือก `-c envName` เพียงอย่างเดียวไม่เพียงพอโดยไม่มีการกำหนดสภาพแวดล้อมที่สอดคล้องกัน

6. **การแยกทรัพยากร**: แต่ละสภาพแวดล้อมสร้างชุดทรัพยากรของตนเอง ช่วยให้คุณสามารถมีสภาพแวดล้อมการพัฒนา การทดสอบ และการผลิตในบัญชี AWS เดียวกันโดยไม่มีความขัดแย้ง

## อื่นๆ

คุณสามารถกำหนดพารามิเตอร์สำหรับการปรับใช้งานได้สองวิธี: โดยใช้ `cdk.json` หรือใช้ไฟล์ `parameter.ts` ที่มีความปลอดภัยด้านประเภท

#### การใช้ cdk.json (วิธีดั้งเดิม)

วิธีดั้งเดิมในการกำหนดค่าพารามิเตอร์คือการแก้ไขไฟล์ `cdk.json` วิธีนี้ง่ายแต่ขาดการตรวจสอบประเภท:

```json
{
  "app": "npx ts-node --prefer-ts-exts bin/bedrock-chat.ts",
  "context": {
    "bedrockRegion": "us-east-1",
    "allowedIpV4AddressRanges": ["0.0.0.0/1", "128.0.0.0/1"],
    "selfSignUpEnabled": true
  }
}
```

#### การใช้ parameter.ts (วิธีที่แนะนำสำหรับความปลอดภัยด้านประเภท)

สำหรับความปลอดภัยและประสบการณ์การพัฒนาที่ดีขึ้น คุณสามารถใช้ไฟล์ `parameter.ts` เพื่อกำหนดพารามิเตอร์ของคุณ:

```typescript
// กำหนดพารามิเตอร์สำหรับสภาพแวดล้อมเริ่มต้น
bedrockChatParams.set("default", {
  bedrockRegion: "us-east-1",
  allowedIpV4AddressRanges: ["192.168.0.0/16"],
  selfSignUpEnabled: true,
});

// กำหนดพารามิเตอร์สำหรับสภาพแวดล้อมเพิ่มเติม
bedrockChatParams.set("dev", {
  bedrockRegion: "us-west-2",
  allowedIpV4AddressRanges: ["10.0.0.0/8"],
  enableRagReplicas: false, // ประหยัดค่าใช้จ่ายสำหรับสภาพแวดล้อมการพัฒนา
});

bedrockChatParams.set("prod", {
  bedrockRegion: "us-east-1",
  allowedIpV4AddressRanges: ["172.16.0.0/12"],
  enableLambdaSnapStart: true,
  enableRagReplicas: true, // เพิ่มความพร้อมใช้งานสำหรับการผลิต
});
```

> [!Note]
> ผู้ใช้ปัจจุบันสามารถยังคงใช้ `cdk.json` ได้โดยไม่มีการเปลี่ยนแปลง วิธีการของ `parameter.ts` แนะนำสำหรับการปรับใช้งานใหม่หรือเมื่อคุณต้องจัดการกับหลายสภาพแวดล้อม

### การปรับใช้งานหลายสภาพแวดล้อม

คุณสามารถปรับใช้งานหลายสภาพแวดล้อมจากโค้ดเดียวกันโดยใช้ไฟล์ `parameter.ts` และตัวเลือก `-c envName`

#### ข้อกำหนดเบื้องต้น

1. กำหนดสภาพแวดล้อมของคุณใน `parameter.ts` ตามที่แสดงข้างต้น
2. แต่ละสภาพแวดล้อมจะมีทรัพยากรของตนเองพร้อมคำนำหน้าเฉพาะสภาพแวดล้อม

#### คำสั่งการปรับใช้งาน

เพื่อปรับใช้งานสภาพแวดล้อมเฉพาะ:

```bash
# ปรับใช้งานสภาพแวดล้อม dev
npx cdk deploy --all -c envName=dev

# ปรับใช้งานสภาพแวดล้อม prod
npx cdk deploy --all -c envName=prod
```

หากไม่ระบุสภาพแวดล้อม จะใช้สภาพแวดล้อม "default":

```bash
# ปรับใช้งานสภาพแวดล้อมเริ่มต้น
npx cdk deploy --all
```

#### หมายเหตุที่สำคัญ

1. **การตั้งชื่อสแต็ก**:

   - สแต็กหลักสำหรับแต่ละสภาพแวดล้อมจะมีคำนำหน้าชื่อด้วยชื่อสภาพแวดล้อม (เช่น `dev-BedrockChatStack`, `prod-BedrockChatStack`)
   - อย่างไรก็ตาม สแต็กบอทแบบกำหนดเองต่างๆ (`BrChatKbStack*`) และสแต็กการเผยแพร่ API (`ApiPublishmentStack*`) จะไม่ได้รับคำนำหน้าสภาพแวดล้อม เนื่องจากถูกสร้างแบบไดนามิกในขณะรันไทม์

2. **การตั้งชื่อทรัพยากร**:

   - เพียงบางทรัพยากรเท่านั้นที่ได้รับคำนำหน้าสภาพแวดล้อมในชื่อ (เช่น ตาราง `dev_ddb_export`, `dev-FrontendWebAcl`)
   - ทรัพยากรส่วนใหญ่คงชื่อเดิม แต่จะแยกออกจากกันโดยอยู่ในสแต็กที่แตกต่างกัน

3. **การระบุสภาพแวดล้อม**:

   - ทรัพยากรทั้งหมดจะถูกติดแท็ก `CDKEnvironment` ที่มีชื่อสภาพแวดล้อม
   - คุณสามารถใช้แท็กนี้เพื่อระบุว่าทรัพยากรใดอยู่ในสภาพแวดล้อมใด
   - ตัวอย่าง: `CDKEnvironment: dev` หรือ `CDKEnvironment: prod`

4. **การแทนที่สภาพแวดล้อมเริ่มต้น**: หากคุณกำหนดสภาพแวดล้อม "default" ใน `parameter.ts` จะแทนที่การตั้งค่าใน `cdk.json` เพื่อใช้ `cdk.json` ต่อไป ไม่ต้องกำหนดสภาพแวดล้อม "default" ใน `parameter.ts`

5. **ข้อกำหนดสภาพแวดล้อม**: เพื่อสร้างสภาพแวดล้อมอื่นนอกเหนือจาก "default" คุณต้องใช้ `parameter.ts` ตัวเลือก `-c envName` เพียงอย่างเดียวไม่เพียงพอโดยไม่มีการกำหนดสภาพแวดล้อมที่สอดคล้องกัน

6. **การแยกทรัพยากร**: แต่ละสภาพแวดล้อมจะสร้างชุดทรัพยากรของตนเอง ช่วยให้คุณสามารถมีสภาพแวดล้อมการพัฒนา การทดสอบ และการผลิตในบัญชี AWS เดียวกันโดยไม่มีความขัดแย้ง

## อื่นๆ

### ลบทรัพยากร

หากใช้ CLI และ CDK ให้ใช้คำสั่ง `npx cdk destroy` หากไม่ใช่ ให้เข้าไปที่ [CloudFormation](https://console.aws.amazon.com/cloudformation/home) แล้วลบ `BedrockChatStack` และ `FrontendWafStack` ด้วยตนเอง โปรดทราบว่า `FrontendWafStack` อยู่ในภูมิภาค `us-east-1`

### การตั้งค่าภาษา

แอสเสทนี้ตรวจจับภาษาโดยอัตโนมัติโดยใช้ [i18next-browser-languageDetector](https://github.com/i18next/i18next-browser-languageDetector) คุณสามารถสลับภาษาได้จากเมนูแอปพลิเคชัน หรือสามารถใช้ Query String เพื่อตั้งภาษาได้ดังนี้

> `https://example.com?lng=ja`

### ปิดการลงทะเบียนด้วยตนเอง

ตัวอย่างนี้เปิดการลงทะเบียนด้วยตนเองตามค่าเริ่มต้น หากต้องการปิดการลงทะเบียนด้วยตนเอง ให้เปิด [cdk.json](./cdk/cdk.json) และเปลี่ยน `selfSignUpEnabled` เป็น `false` หากคุณกำหนดค่า [ผู้ให้บริการยืนยันตัวตนภายนอก](#external-identity-provider) ค่านี้จะถูกละเว้นและปิดใช้งานโดยอัตโนมัติ

### จำกัดโดเมนสำหรับที่อยู่อีเมลในการลงทะเบียน

ตามค่าเริ่มต้น ตัวอย่างนี้ไม่จำกัดโดเมนสำหรับที่อยู่อีเมลในการลงทะเบียน หากต้องการอนุญาตให้ลงทะเบียนเฉพาะโดเมนที่ระบุ ให้เปิด `cdk.json` และระบุโดเมนเป็นรายการใน `allowedSignUpEmailDomains`

```ts
"allowedSignUpEmailDomains": ["example.com"],
```

### ผู้ให้บริการยืนยันตัวตนภายนอก

ตัวอย่างนี้รองรับผู้ให้บริการยืนยันตัวตนภายนอก ปัจจุบันรองรับ [Google](./idp/SET_UP_GOOGLE_th-TH.md) และ [ผู้ให้บริการ OIDC แบบกำหนดเอง](./idp/SET_UP_CUSTOM_OIDC_th-TH.md)

### เพิ่มผู้ใช้ใหม่ในกลุ่มโดยอัตโนมัติ

ตัวอย่างนี้มีกลุ่มต่อไปนี้เพื่อให้สิทธิ์กับผู้ใช้:

- [`Admin`](./ADMINISTRATOR_th-TH.md)
- [`CreatingBotAllowed`](#bot-personalization)
- [`PublishAllowed`](./PUBLISH_API_th-TH.md)

หากคุณต้องการให้ผู้ใช้ที่สร้างใหม่เข้าร่วมกลุ่มโดยอัตโนมัติ คุณสามารถระบุได้ใน [cdk.json](./cdk/cdk.json)

```json
"autoJoinUserGroups": ["CreatingBotAllowed"],
```

ตามค่าเริ่มต้น ผู้ใช้ที่สร้างใหม่จะเข้าร่วมกลุ่ม `CreatingBotAllowed`

### กำหนดค่าการทำซ้ำของ RAG

`enableRagReplicas` เป็นตัวเลือกใน [cdk.json](./cdk/cdk.json) ที่ควบคุมการตั้งค่าการทำซ้ำสำหรับฐานข้อมูล RAG โดยเฉพาะ Knowledge Bases ที่ใช้ Amazon OpenSearch Serverless ซึ่งส่งผลกระทบต่อฐานข้อมูลบอทสโตร์ด้วย

- **ค่าเริ่มต้น**: true
- **true**: เพิ่มความพร้อมใช้งานโดยเปิดใช้งานการทำซ้ำเพิ่มเติม เหมาะสำหรับสภาพแวดล้อมการผลิต แต่เพิ่มค่าใช้จ่าย
- **false**: ลดค่าใช้จ่ายโดยใช้การทำซ้ำน้อยลง เหมาะสำหรับการพัฒนาและทดสอบ

นี่เป็นการตั้งค่าระดับบัญชี/ภูมิภาค ส่งผลกระทบต่อแอปพลิเคชันทั้งหมดแทนที่จะเป็นบอทแต่ละตัว

> [!หมายเหตุ]
> ตั้งแต่เดือนมิถุนายน 2024 Amazon OpenSearch Serverless รองรับ 0.5 OCU ซึ่งลดค่าเริ่มต้นสำหรับเวิร์กโหลดขนาดเล็ก การปรับใช้งานผลิตสามารถเริ่มต้นที่ 2 OCUs ในขณะที่เวิร์กโหลดการพัฒนา/ทดสอบสามารถใช้ 1 OCU OpenSearch Serverless จะปรับขนาดโดยอัตโนมัติตามความต้องการของเวิร์กโหลด สำหรับรายละเอียดเพิ่มเติม โปรดเยี่ยมชม[ประกาศ](https://aws.amazon.com/jp/about-aws/whats-new/2024/06/amazon-opensearch-serverless-entry-cost-half-collection-types/)

(ส่วนที่เหลือจะแปลต่อไปในรูปแบบเดียวกัน)

## ผู้ติดต่อ

- [Takehiro Suzuki](https://github.com/statefb)
- [Yusuke Wada](https://github.com/wadabee)
- [Yukinobu Mine](https://github.com/Yukinobu-Mine)

## 🏆 ผู้มีส่วนร่วมสำคัญ

- [fsatsuki](https://github.com/fsatsuki)
- [k70suK3-k06a7ash1](https://github.com/k70suK3-k06a7ash1)

## ผู้มีส่วนร่วม

[![ผู้มีส่วนร่วมของ bedrock chat](https://contrib.rocks/image?repo=aws-samples/bedrock-chat&max=1000)](https://github.com/aws-samples/bedrock-chat/graphs/contributors)

## สัญญาอนุญาต

ไลบรารีนี้อยู่ภายใต้ใบอนุญาต MIT-0 ดูที่[ไฟล์สัญญาอนุญาต](./LICENSE)