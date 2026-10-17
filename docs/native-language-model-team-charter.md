# GBSBFORYOU Native Language Model — Team Charter
**स्थिति:** प्रस्तावित कार्य-संरचना (Draft v0.1)  
**परियोजना स्वामी:** GBSBFORYOU  
**उद्देश्य:** मोबाइल से संचालित अनुसंधान और मानवीय निगरानी के माध्यम से अपना छोटा भाषा मॉडल शून्य से प्रशिक्षित करने की व्यवहार्यता जाँचना।

> यह योजना है, कार्यशील 12-agent प्रणाली या प्रशिक्षित मॉडल के अस्तित्व का दावा नहीं। AI एजेंट प्रस्ताव, कोड और विश्लेषण देंगे; महत्त्वपूर्ण निर्णय मानव स्वीकृति के अधीन होंगे।

## 1. परियोजना के सिद्धांत
1. **ईमानदार स्वदेशी दावा:** विदेशी मॉडल के वेट्स से शुरू मॉडल को अपना मूल मॉडल नहीं कहा जाएगा। शून्य से प्रशिक्षण के दावे के लिए प्रारंभिक वेट्स, डेटा, प्रशिक्षण कोड और लॉग दर्ज होंगे।
2. **प्रदाता-स्वतंत्रता:** विकास में उपयोग किए गए AI सहायक और अंतिम प्रशिक्षित भाषा मॉडल अलग-अलग दर्ज होंगे।
3. **मोबाइल-प्रथम संचालन:** मोबाइल से निर्देश, समीक्षा, दस्तावेज़ीकरण और GitHub प्रबंधन; भारी प्रशिक्षण केवल उपलब्ध और स्वीकृत कंप्यूटिंग पर।
4. **डेटा अधिकार:** प्रत्येक स्रोत के लिए URL, प्राप्ति तिथि, लाइसेंस/उपयोग-अधिकार और बहिष्करण स्थिति दर्ज हो।
5. **मानव अनुमोदन:** डेटा रिलीज़, बड़े compute खर्च, training runs और model release के लिए मानव अनुमोदन आवश्यक।
6. **पुनरुत्पादकता:** कोड संस्करण, configuration, dataset manifest, logs, checkpoints और evaluation results सुरक्षित रखें।
7. **सुरक्षा:** API keys, credentials या संवेदनशील डेटा GitHub में commit न करें।
8. **अलग उत्पाद सीमाएँ:** यह भाषा-मॉडल अनुसंधान, मौजूदा AI Guru API का विकल्प नहीं है। API का वर्तमान rule-based scaffold अलग सत्यापन तक production AI tutor नहीं माना जाएगा।

## 2. चार मानव पद

### H1 — Research & Architecture Supervisor
**उद्देश्य:** अनुसंधान दिशा, तकनीकी विकल्प और व्यवहार्यता नियंत्रित करना।  
**जिम्मेदारियाँ:** शोध-स्रोतों की समीक्षा; मॉडल आकार/आर्किटेक्चर प्रस्ताव; तकनीकी निर्णय रजिस्टर; compute अनुमान; एजेंट 1–3 की समीक्षा।  
**आवश्यक कौशल:** ML/AI की समझ, शोध-स्रोत मूल्यांकन, तकनीकी दस्तावेज़ीकरण।  
**स्वीकृति-द्वार:** आर्किटेक्चर और compute योजना लिखित प्रमाणों के बिना आगे न बढ़े।

### H2 — Data & Language Supervisor
**उद्देश्य:** वैध, प्रासंगिक और गुणवत्ता-जाँचा प्रशिक्षण डेटा तैयार करना।  
**जिम्मेदारियाँ:** डेटा-स्रोत रजिस्टर; लाइसेंस समीक्षा; deduplication और गुणवत्ता नियम; हिंदी/भारतीय भाषा परीक्षण; एजेंट 4–6 की समीक्षा।  
**आवश्यक कौशल:** डेटा प्रबंधन, भाषा संसाधन, लाइसेंस और गोपनीयता की समझ।  
**स्वीकृति-द्वार:** स्रोत और उपयोग-अधिकार दर्ज हुए बिना कोई dataset प्रशिक्षण में शामिल न हो।

### H3 — Model Engineering Supervisor
**उद्देश्य:** मॉडल कोड, प्रशिक्षण प्रक्रिया और प्रयोगों को सुरक्षित व पुनरुत्पादित करने योग्य बनाना।  
**जिम्मेदारियाँ:** code review; tokenizer/model implementation; training scripts; checkpoints; resource monitoring; एजेंट 7–9 की समीक्षा।  
**आवश्यक कौशल:** Python, PyTorch या समकक्ष framework, testing, ML training।  
**स्वीकृति-द्वार:** परीक्षण, resource budget और checkpoint/rollback योजना के बिना training run न शुरू हो।

### H4 — Quality, Safety & Documentation Supervisor
**उद्देश्य:** गुणवत्ता, सुरक्षा, लाइसेंस और दस्तावेज़ीकरण का स्वतंत्र नियंत्रण।  
**जिम्मेदारियाँ:** evaluation protocol; data leakage जाँच; सुरक्षा/लाइसेंस समीक्षा; release checklist; एजेंट 10–12 की समीक्षा।  
**आवश्यक कौशल:** परीक्षण, जोखिम मूल्यांकन, डेटा/सॉफ्टवेयर लाइसेंस, दस्तावेज़ीकरण।  
**स्वीकृति-द्वार:** परीक्षण रिपोर्ट और ज्ञात सीमाओं के बिना मॉडल को रिलीज़/शैक्षणिक उपयोग की स्वीकृति न मिले।

### परियोजना निदेशक / मालिक
परियोजना मालिक scope, बजट, प्राथमिकता और अंतिम go/no-go निर्णय करेगा। यह चार पर्यवेक्षकों से अलग शासन-भूमिका है। हर पर्यवेक्षक अपने क्षेत्र के लिए जवाबदेह होगा।

## 3. बारह AI एजेंट प्रोफाइल

### A1 — Research Scout
- **मिशन:** मूल भाषा मॉडल, tokenizer, training, evaluation और भारतीय भाषा अनुसंधान के प्राथमिक स्रोत ढूँढना।
- **आउटपुट:** स्रोत-सहित evidence brief, तारीख, दावे की सीमा और खुले प्रश्न।
- **निषेध:** बिना स्रोत तथ्य, benchmark या सरकारी समर्थन का दावा न करे।
- **मानव समीक्षा:** H1.

### A2 — Architecture Analyst
- **मिशन:** छोटे decoder-only Transformer सहित विकल्पों की तुलना और architecture proposal बनाना।
- **आउटपुट:** config, parameter estimate, context length, tokenizer assumptions और risks।
- **निषेध:** compute estimate के बिना मॉडल आकार अंतिम न माने।
- **मानव समीक्षा:** H1.

### A3 — Compute & Cost Planner
- **मिशन:** RAM/VRAM, storage, training duration और लागत का अनुमान बनाना।
- **आउटपुट:** न्यूनतम/मध्यम/विस्तारित संसाधन तालिका और assumptions।
- **निषेध:** मुफ्त GPU या सरकारी compute की उपलब्धता की गारंटी न दे।
- **मानव समीक्षा:** H1.

### A4 — Data Discovery Agent
- **मिशन:** हिंदी/भारतीय भाषा और तकनीकी पाठ के संभावित स्रोत खोजना।
- **आउटपुट:** dataset manifest—URL, भाषा, अनुमानित आकार, लाइसेंस स्थिति, तिथि और जोखिम।
- **निषेध:** अनधिकृत या प्रतिबंधित स्रोत से सामग्री न निकाले।
- **मानव समीक्षा:** H2.

### A5 — Data Quality & Dedup Agent
- **मिशन:** भाषा पहचान, दोहराव, format और गुणवत्ता नियम लागू करना।
- **आउटपुट:** reproducible scripts, quality report और excluded-data log।
- **निषेध:** स्रोत/लाइसेंस metadata हटाकर सामग्री को training-ready घोषित न करे।
- **मानव समीक्षा:** H2.

### A6 — Tokenizer & Language Agent
- **मिशन:** देवनागरी, मात्राओं, विरामचिह्न, अंकों और code-mixed text के लिए tokenizer प्रयोगों की योजना।
- **आउटपुट:** tokenizer config, coverage/sequence-length tests और उदाहरण।
- **निषेध:** tokenizer को भाषा-समझ का पूरा प्रमाण न बताए।
- **मानव समीक्षा:** H2.

### A7 — Model Implementation Agent
- **मिशन:** चुनी गई architecture के अनुरूप स्पष्ट, परीक्षण योग्य model code तैयार करना।
- **आउटपुट:** code, unit tests, config schema और parameter count।
- **निषेध:** समीक्षा के बिना production secrets या अनजान dependencies न जोड़े।
- **मानव समीक्षा:** H3.

### A8 — Training Pipeline Agent
- **मिशन:** data loading, batching, optimizer, logging, checkpoints और resume/stop logic तैयार करना।
- **आउटपुट:** reproducible training script, config, logs और recovery instructions।
- **निषेध:** budget limit या stop conditions के बिना run न शुरू करे।
- **मानव समीक्षा:** H3.

### A9 — Instruction Data Agent
- **मिशन:** लाइसेंस-अनुमत उदाहरणों से instruction-format dataset और train/evaluation split की योजना।
- **आउटपुट:** schema, sample records, quality rules और leakage prevention plan।
- **निषेध:** synthetic examples को प्रमाणित वास्तविक परिणाम के रूप में प्रस्तुत न करे।
- **मानव समीक्षा:** H3 और H4.

### A10 — Evaluation Agent
- **मिशन:** held-out tests पर language modeling loss/perplexity जहाँ उपयुक्त हो, हिंदी गुणवत्ता, instruction following और coding tests चलाना।
- **आउटपुट:** reproducible benchmark report, failure examples और limitations।
- **निषेध:** छोटे benchmark को व्यापक बुद्धिमत्ता या production readiness का प्रमाण न बताए।
- **मानव समीक्षा:** H4.

### A11 — Safety, Privacy & License Agent
- **मिशन:** data/license/privacy risks, secrets और release obligations की जाँच।
- **आउटपुट:** risk register, remediation list और release checklist।
- **निषेध:** अस्पष्ट अधिकारों को “स्वीकृत” न चिह्नित करे; मानव/विशेषज्ञ समीक्षा आवश्यक रहे।
- **मानव समीक्षा:** H4.

### A12 — Experiment & Documentation Agent
- **मिशन:** प्रयोगों, निर्णयों, versions, datasets, checkpoints और परिणामों का index रखना।
- **आउटपुट:** experiment log, model-card draft, changelog और reproducibility checklist।
- **निषेध:** अनुपस्थित परिणाम या उपलब्धि गढ़े नहीं।
- **मानव समीक्षा:** H4.

## 4. साझा task-card schema
हर कार्य में ये फ़ील्ड हों:
- task_id
- owner_agent
- human_supervisor
- objective
- inputs_and_sources
- expected_artifact
- acceptance_criteria
- risk_level
- status: backlog / in_progress / review / blocked / accepted
- evidence
- reviewer_decision
- next_action

एजेंट स्वयं अपने परिणाम को accepted नहीं कर सकता। स्वीकृति संबंधित मानव पर्यवेक्षक देगा।

## 5. पहले चरण की सफलता की परिभाषा
प्रथम चरण का लक्ष्य “ChatGPT जैसा मॉडल” नहीं है। सफलता तब मानी जाएगी जब:
1. छोटा Transformer और tokenizer शून्य से बनाए/कॉन्फ़िगर किए गए हों;
2. प्रशिक्षण डेटा के स्रोत और अधिकार दर्ज हों;
3. training run पूरा हो और checkpoints सुरक्षित हों;
4. held-out evaluation दोहराई जा सके;
5. परिणाम, सीमाएँ और लागत लिखित हों;
6. दावे वास्तविक प्रमाण से आगे न जाएँ।

## 6. प्रारंभिक दायरा
- प्रथम प्रयोग: छोटा हिंदी-केंद्रित भाषा मॉडल; अंतिम parameter count compute audit के बाद तय होगा।
- लक्ष्य: training pipeline की व्यवहार्यता प्रमाणित करना, न कि पहले चरण में general-purpose assistant बनाना।
- AI Guru API और School OS का मौजूदा कोड अलग समीक्षा के बिना नहीं बदलेगा।
- कोई API key, निजी डेटा या credentials repository में नहीं रखे जाएँगे।
