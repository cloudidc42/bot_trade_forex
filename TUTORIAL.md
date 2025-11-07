# 📚 TUTORIAL - Multi-Asset Trading Bot (100 ขั้นตอน)

> คู่มือแบบ Step-by-Step ครบถ้วน ตั้งแต่พื้นฐานจนถึง Production

**เวอร์ชัน**: 1.0.0
**อัพเดทล่าสุด**: 2024-01-15
**ระดับ**: Beginner → Advanced
**ระยะเวลาโดยประมาณ**: 30-60 วัน (ขึ้นกับความสามารถและเวลาที่ใช้)

---

## 🎯 ภาพรวมคู่มือ

คู่มือนี้จะพาคุณสร้างระบบ **Multi-Asset Algorithmic Trading Bot** แบบครบวงจรตั้งแต่เริ่มต้น ครอบคลุม:

- **Forex** - การเทรดสกุลเงิน (EUR/USD, GBP/USD, ฯลฯ)
- **Cryptocurrency** - สกุลเงินดิจิทัล (Bitcoin, Ethereum, ฯลฯ)
- **Stocks** - หุ้นบริษัท (AAPL, TSLA, SPY, ฯลฯ)
- **Commodities** - สินค้าโภคภัณฑ์ (ทอง, น้ำมัน, เงิน)

### 🏁 เป้าหมายสุดท้าย

หลังจากทำตามคู่มือครบ 100 ขั้นตอน คุณจะมี:

1. ✅ ระบบเทรดอัตโนมัติที่รันได้จริง
2. ✅ Backtesting framework พร้อม performance metrics
3. ✅ Risk management system แบบมืออาชีพ
4. ✅ Monitoring & alerting ครบถ้วน
5. ✅ Production-ready deployment บน Docker
6. ✅ ความรู้ด้าน algorithmic trading แบบลึกซึ้ง

---

## 📖 โครงสร้างคู่มือ (10 ส่วน)

คู่มือนี้แบ่งเป็น **10 Parts** ดังนี้:

### 📘 [PART 01: พื้นฐานและตั้งค่าสภาพแวดล้อม](docs/PART01.md) - ขั้นที่ 1-10

**สิ่งที่จะได้เรียนรู้:**
- เข้าใจ algorithmic trading และ สินทรัพย์ต่างๆ
- ตั้งค่า Python environment และ dependencies
- สร้างโครงสร้างโปรเจค
- Config management (routing.yml, risk.yml)
- ดาวน์โหลดและจัดเก็บข้อมูลตลาด

**เวลาโดยประมาณ**: 2-3 วัน
**ความยาก**: ⭐ Beginner

---

### 📗 [PART 02: Data Feeders และ Market Data](docs/PART02.md) - ขั้นที่ 11-20

**สิ่งที่จะได้เรียนรู้:**
- สร้าง Yahoo Finance feeder (หุ้น/ทอง/น้ำมัน)
- สร้าง CCXT feeder (คริปโต)
- สร้าง MetaTrader 5 feeder (Forex)
- Data normalization และ cleaning
- Caching mechanism ด้วย Parquet

**เวลาโดยประมาณ**: 3-4 วัน
**ความยาก**: ⭐⭐ Intermediate

---

### 📙 [PART 03: Strategy Design พื้นฐาน](docs/PART03.md) - ขั้นที่ 21-30

**สิ่งที่จะได้เรียนรู้:**
- Base strategy class design
- MA Crossover strategy (Simple และ Exponential)
- RSI Mean Reversion strategy
- Breakout strategy
- Technical indicators (pandas_ta, ta)
- Signal generation และ validation

**เวลาโดยประมาณ**: 4-5 วัน
**ความยาก**: ⭐⭐ Intermediate

---

### 📕 [PART 04: Backtesting Framework](docs/PART04.md) - ขั้นที่ 31-40

**สิ่งที่จะได้เรียนรู้:**
- VectorBT integration (vectorized backtesting)
- Backtrader integration (event-driven)
- Performance metrics (Sharpe, Sortino, MaxDD)
- Walk-forward analysis
- Monte Carlo simulation
- Multi-asset portfolio backtesting

**เวลาโดยประมาณ**: 5-7 วัน
**ความยาก**: ⭐⭐⭐ Advanced

---

### 📓 [PART 05: Risk Management & Position Sizing](docs/PART05.md) - ขั้นที่ 41-50

**สิ่งที่จะได้เรียนรู้:**
- Position sizing (Fixed %, ATR-based, Kelly)
- Volatility targeting
- Portfolio-level limits (max drawdown, daily loss)
- Asset class exposure limits
- Correlation checks
- Circuit breakers

**เวลาโดยประมาณ**: 4-5 วัน
**ความยาก**: ⭐⭐⭐ Advanced

---

### 📔 [PART 06: Portfolio & Routing](docs/PART06.md) - ขั้นที่ 51-60

**สิ่งที่จะได้เรียนรู้:**
- Portfolio manager implementation
- Position tracking และ PnL calculation
- Asset → Exchange/Broker routing
- Multi-asset rebalancing
- Portfolio optimization
- Risk parity allocation

**เวลาโดยประมาณ**: 4-5 วัน
**ความยาก**: ⭐⭐⭐ Advanced

---

### 📒 [PART 07: Order Execution & Broker Integration](docs/PART07.md) - ขั้นที่ 61-70

**สิ่งที่จะได้เรียนรู้:**
- CCXT order client (Binance, Coinbase)
- MT5 order client (Forex)
- Alpaca API (US Stocks)
- Order management system
- Fill tracking และ reconciliation
- Slippage และ fee calculation

**เวลาโดยประมาณ**: 5-7 วัน
**ความยาก**: ⭐⭐⭐⭐ Expert

---

### 📃 [PART 08: Monitoring & Observability](docs/PART08.md) - ขั้นที่ 71-80

**สิ่งที่จะได้เรียนรู้:**
- Prometheus metrics collection
- Grafana dashboards สำหรับ portfolio performance
- Loki log aggregation
- Alert system (Telegram, Email)
- Health checks และ heartbeat
- System resource monitoring

**เวลาโดยประมาณ**: 3-4 วัน
**ความยาก**: ⭐⭐⭐ Advanced

---

### 📄 [PART 09: Deployment & Production](docs/PART09.md) - ขั้นที่ 81-90

**สิ่งที่จะได้เรียนรู้:**
- Docker containerization
- Docker Compose orchestration
- Database setup (PostgreSQL)
- CI/CD pipeline (GitHub Actions)
- Security hardening
- Paper trading → Live trading transition
- Runbook และ emergency procedures

**เวลาโดยประมาณ**: 5-7 วัน
**ความยาก**: ⭐⭐⭐⭐ Expert

---

### 📰 [PART 10: Advanced Topics & Optimization](docs/PART10.md) - ขั้นที่ 91-100

**สิ่งที่จะได้เรียนรู้:**
- Regime detection (HMM, ML)
- Strategy ensemble methods
- Machine learning integration
- Multi-venue arbitrage
- Derivatives support (Futures, Options)
- Performance optimization
- Advanced portfolio techniques

**เวลาโดยประมาณ**: 7-10 วัน
**ความยาก**: ⭐⭐⭐⭐⭐ Expert+

---

## 🎓 แนะนำสำหรับผู้เริ่มต้น

### ข้อกำหนดเบื้องต้น (Prerequisites)

#### ความรู้พื้นฐาน

| หัวข้อ | ระดับที่ต้องการ | ทางเลือก |
|--------|----------------|----------|
| Python | Intermediate | เรียน Python ก่อน 1-2 สัปดาห์ |
| pandas & numpy | Basic | เรียนพร้อมกับคู่มือได้ |
| Git | Basic | ใช้ GitHub Desktop ก็ได้ |
| Trading Basics | None | จะสอนในคู่มือ |
| Docker | None | จะสอนในคู่มือ |

#### ฮาร์ดแวร์

```
CPU:       2+ cores (4+ แนะนำ)
RAM:       4+ GB (8+ แนะนำ)
Storage:   20+ GB SSD
OS:        Windows/Mac/Linux
Network:   Stable broadband
```

#### ซอฟต์แวร์

- Python 3.11+
- Git
- Docker & Docker Compose
- VSCode หรือ IDE อื่นๆ
- MetaTrader 5 (optional สำหรับ Forex)

### การใช้คู่มือนี้

#### 🎯 แนวทางการเรียนรู้

**สำหรับผู้เริ่มต้น**:
1. เริ่มจาก PART01 และทำตามลำดับ
2. **อย่าข้ามขั้นตอน** - แต่ละขั้นสร้างบนขั้นก่อนหน้า
3. ทำแบบฝึกหัดทุกข้อ
4. ทดลองโค้ดด้วยตัวเอง
5. ถามคำถามใน community

**สำหรับผู้มีประสบการณ์**:
1. อ่านภาพรวมใน README.md และ SUMMARY.md
2. ข้ามไปยัง PART ที่สนใจได้เลย
3. Focus ที่ advanced topics (PART 08-10)
4. ปรับแต่งระบบตามความต้องการ

#### ⏱️ ตารางเวลาแนะนำ

**Full-time (30 วัน)**:
- สัปดาห์ 1: PART 01-03 (Setup + Data + Strategy)
- สัปดาห์ 2: PART 04-05 (Backtest + Risk)
- สัปดาห์ 3: PART 06-07 (Portfolio + Execution)
- สัปดาห์ 4: PART 08-10 (Monitoring + Deploy + Advanced)

**Part-time (60 วัน)**:
- สัปดาห์ 1-2: PART 01-02
- สัปดาห์ 3-4: PART 03-04
- สัปดาห์ 5-6: PART 05-06
- สัปดาห์ 7-8: PART 07-10

---

## 📊 สรุปเนื้อหาทั้ง 100 ขั้นตอน

### 🟦 Phase 1: Foundation (ขั้นที่ 1-20)

#### ขั้นที่ 1-10: Setup & Basics

1. ภาพรวม Algorithmic Trading และ Multi-Asset Trading
2. เข้าใจสินทรัพย์แต่ละประเภท (Forex/Crypto/Stocks/Commodities)
3. ติดตั้ง Python 3.11+ และสร้าง virtual environment
4. ติดตั้ง dependencies จาก requirements.txt
5. สร้างโครงสร้างโฟลเดอร์โปรเจค
6. ตั้งค่า configs/routing.yml (asset routing)
7. ตั้งค่า configs/risk.yml (risk parameters)
8. ตั้งค่า .env (environment variables)
9. เข้าใจ data flow architecture
10. ดาวน์โหลดข้อมูลทดสอบ (3 assets, 3 ปี)

#### ขั้นที่ 11-20: Data Feeders

11. ออกแบบ Base Feeder class (Abstract)
12. สร้าง Yahoo Finance feeder (yfinance)
13. ดึงข้อมูล Stocks (AAPL, TSLA, SPY)
14. ดึงข้อมูล Commodities (GLD ทอง, USO น้ำมัน)
15. สร้าง CCXT feeder สำหรับ Crypto
16. เชื่อมต่อ Binance และดึงข้อมูล BTC/ETH
17. สร้าง MT5 feeder สำหรับ Forex (optional)
18. Data normalization (timezone, columns, format)
19. Caching mechanism ด้วย Parquet files
20. Data validation และ quality checks

---

### 🟩 Phase 2: Strategy & Backtesting (ขั้นที่ 21-40)

#### ขั้นที่ 21-30: Strategy Design

21. ออกแบบ Base Strategy class
22. Strategy interface (entry/exit signals)
23. สร้าง Technical Indicators wrapper (pandas_ta)
24. MA Crossover Strategy - Simple Moving Average
25. MA Crossover Strategy - Exponential Moving Average
26. RSI Mean Reversion Strategy
27. Bollinger Bands Mean Reversion
28. Breakout Strategy (Support/Resistance)
29. Multi-timeframe analysis
30. Regime detection (Trend vs Range)

#### ขั้นที่ 31-40: Backtesting Framework

31. ติดตั้งและตั้งค่า VectorBT
32. สร้าง VectorBT runner พื้นฐาน
33. Backtest MA Crossover บน 1 asset
34. คำนวณ Performance Metrics (Sharpe, MaxDD, Win Rate)
35. Portfolio backtest (multi-asset)
36. Walk-Forward Analysis implementation
37. Parameter optimization (grid search)
38. Monte Carlo Simulation
39. Out-of-sample validation
40. Generate backtest reports (CSV + Charts)

---

### 🟨 Phase 3: Risk & Portfolio (ขั้นที่ 41-60)

#### ขั้นที่ 41-50: Risk Management

41. Position sizing - Fixed Fractional
42. Position sizing - ATR-based
43. Position sizing - Volatility Targeting
44. Position sizing - Kelly Criterion
45. Portfolio-level risk limits
46. Daily/Weekly/Monthly loss limits
47. Max position size และ exposure limits
48. Correlation-based risk management
49. Circuit breakers implementation
50. Drawdown monitoring และ auto-pause

#### ขั้นที่ 51-60: Portfolio Management

51. Portfolio Manager class design
52. Position tracking (open/closed)
53. PnL calculation (realized/unrealized)
54. Asset routing logic
55. Multi-asset rebalancing
56. Portfolio optimization (mean-variance)
57. Risk parity allocation
58. Asset allocation strategies
59. Portfolio analytics และ reporting
60. Performance attribution analysis

---

### 🟧 Phase 4: Execution & Live Trading (ขั้นที่ 61-80)

#### ขั้นที่ 61-70: Order Execution

61. Order routing architecture
62. CCXT client - Binance integration
63. CCXT client - Order placement (Market/Limit)
64. MT5 client - Forex connection
65. MT5 client - Order execution
66. Alpaca API - US Stocks integration
67. Order Management System (OMS)
68. Fill tracking และ reconciliation
69. Slippage modeling
70. Execution quality analysis

#### ขั้นที่ 71-80: Monitoring & Observability

71. Prometheus setup และ metrics definition
72. Portfolio performance metrics export
73. Execution metrics export
74. System health metrics
75. Grafana dashboard - Portfolio Performance
76. Grafana dashboard - System Health
77. Loki log aggregation
78. Alert system - Telegram integration
79. Alert system - Email alerts
80. Health checks และ auto-restart

---

### 🟪 Phase 5: Production & Advanced (ขั้นที่ 81-100)

#### ขั้นที่ 81-90: Deployment

81. Docker setup และ Dockerfile
82. Docker Compose configuration
83. PostgreSQL database setup
84. Database schema และ migrations
85. Paper trading mode implementation
86. Live trading mode (micro capital)
87. CI/CD pipeline (GitHub Actions)
88. Security audit และ hardening
89. Backup และ disaster recovery
90. Production runbook และ emergency procedures

#### ขั้นที่ 91-100: Advanced Topics

91. Regime Detection (HMM models)
92. Strategy Ensemble methods
93. Machine Learning integration (sklearn)
94. Feature engineering framework
95. Reinforcement Learning basics
96. Multi-venue arbitrage
97. Futures และ Derivatives support
98. Performance optimization (Cython/Numba)
99. Advanced portfolio techniques
100. Final review และ next steps

---

## 🛠️ เครื่องมือที่ใช้

### Technology Stack

**ภาษา**:
- Python 3.11+
- SQL (PostgreSQL)
- YAML (Config files)
- Markdown (Documentation)

**Data & Analysis**:
- pandas, numpy - Data manipulation
- yfinance - Stock/ETF/Commodity data
- ccxt - Cryptocurrency exchanges
- MetaTrader5 - Forex data/execution

**Backtesting**:
- VectorBT - Vectorized backtesting
- Backtrader - Event-driven backtesting
- FreqTrade - Crypto bot framework

**Technical Indicators**:
- pandas_ta - 130+ indicators
- ta - Technical analysis library

**Database**:
- PostgreSQL - Primary database
- SQLite - Development/testing
- Parquet - Columnar storage

**Monitoring**:
- Prometheus - Metrics collection
- Grafana - Visualization
- Loki - Log aggregation

**Infrastructure**:
- Docker - Containerization
- Docker Compose - Orchestration
- GitHub Actions - CI/CD

---

## 📐 ตัวอย่างไดอะแกรมที่ใช้ในคู่มือ

### System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                   MULTI-ASSET TRADING BOT                         │
└──────────────────────────────────────────────────────────────────┘

┌─────────────┐  OHLCV   ┌─────────────┐  Signals  ┌─────────────┐
│   Feeders   │◄─────────│  Exchanges  │───────────►│  Strategy   │
│(Yahoo/CCXT) │          │   /Brokers  │           │   Engine    │
└──────┬──────┘          └─────────────┘           └──────┬──────┘
       │                                                    │
       │ normalized data                        sizing/risk│
       ▼                                                    ▼
┌─────────────┐                                   ┌─────────────┐
│    Cache    │                                   │  Portfolio  │
│  (Parquet)  │                                   │   Manager   │
└─────────────┘                                   └──────┬──────┘
                                                         │
                                             route/execute
                                                         ▼
┌─────────────┐  metrics   ┌─────────────┐   orders  ┌─────────────┐
│ Monitoring  │◄───────────│  Backtest   │──────────►│   Broker    │
│(Prom/Graf)  │            │   Engine    │           │  Connector  │
└─────────────┘            └─────────────┘           └─────────────┘
```

---

## ✅ แบบฝึกหัดและเกณฑ์ผ่าน

แต่ละ PART จะมี:

### 📝 แบบฝึกหัด (Exercises)

ทุก Part มีแบบฝึกหัด 5-10 ข้อ เช่น:

**PART 01 - Exercise 1:**
> ดาวน์โหลดข้อมูล 3 สินทรัพย์ (AAPL, BTC/USDT, GLD) ย้อนหลัง 3 ปี และบันทึกเป็น Parquet

**PART 04 - Exercise 3:**
> Backtest MA Crossover strategy บน portfolio 5 สินทรัพย์ และต้องได้ Sharpe Ratio > 1.0

### ✅ เกณฑ์ผ่าน (Pass Criteria)

**PART 01**:
- [ ] โปรเจคมีโครงสร้างครบถ้วน
- [ ] ดาวน์โหลดข้อมูล 3 assets สำเร็จ
- [ ] Config files ทำงานได้

**PART 04**:
- [ ] Backtest ทำงานได้สำหรับ 1 strategy
- [ ] ได้ performance metrics ครบถ้วน
- [ ] Win rate > 45%, Sharpe > 0.8

**PART 09**:
- [ ] Docker container รันได้
- [ ] Paper trading 1 สัปดาห์สำเร็จ
- [ ] Monitoring dashboard ทำงาน

---

## ⚠️ คำเตือนและข้อควรระวัง

### 🚨 Risk Warnings

1. **การเทรดมีความเสี่ยง** - อาจสูญเสียเงินทุนทั้งหมด
2. **ทดสอบให้ดี** - Backtest และ paper trading ก่อนใช้เงินจริง
3. **เริ่มเล็กๆ** - ใช้เงินน้อยๆ ก่อน แล้วค่อย scale up
4. **Monitor อย่างใกล้ชิด** - ติดตามระบบตลอดเวลา
5. **ไม่ใช่ holy grail** - ไม่มีกลยุทธ์ไหนชนะตลอดกาล

### 💡 Best Practices

- **เขียน tests** - Unit tests ช่วยจับ bugs ก่อนจะพัง
- **Version control** - Commit บ่อยๆ, branch สำหรับ features ใหม่
- **Logging** - Log ทุกอย่างที่สำคัญ
- **Backup** - สำรอง config และ database เป็นประจำ
- **Documentation** - เขียน docs ให้ตัวเองอ่านภายหลัง

---

## 🎖️ ระดับความรู้

### Beginner (PART 01-03)
- ✅ เข้าใจพื้นฐาน Python
- ✅ ดึงและจัดการข้อมูลตลาดได้
- ✅ สร้างกลยุทธ์เทรดง่ายๆ ได้

### Intermediate (PART 04-06)
- ✅ Backtest กลยุทธ์ได้อย่างถูกต้อง
- ✅ เข้าใจและใช้ risk management
- ✅ จัดการ portfolio หลายสินทรัพย์ได้

### Advanced (PART 07-09)
- ✅ เชื่อมต่อกับ broker/exchange ได้
- ✅ Deploy ระบบขึ้น production
- ✅ Monitor และแก้ไขปัญหาได้

### Expert (PART 10)
- ✅ ใช้ machine learning ในกลยุทธ์
- ✅ Optimize performance ระดับสูง
- ✅ พัฒนาฟีเจอร์ advanced ได้เอง

---

## 📞 การสนับสนุน

### Community & Help

- 💬 **Discord**: [Join our server](https://discord.gg/tradingbot) - ถามคำถามได้
- 📧 **Email**: support@tradingbot.com - สำหรับคำถามเฉพาะ
- 🐛 **Issues**: [GitHub Issues](https://github.com/repo/issues) - รายงาน bugs

### Resources

- 📖 [API Documentation](docs/API.md)
- 🎥 [Video Tutorials](https://youtube.com/playlist)
- 📝 [Blog & Articles](https://blog.tradingbot.com)
- 🗣️ [Community Forum](https://forum.tradingbot.com)

---

## 🗺️ แผนการเรียนรู้

### Week 1-2: Foundation
- อ่าน README.md และ SUMMARY.md
- ทำ PART 01 และ PART 02
- ดาวน์โหลดข้อมูลและทดลองเล่น

### Week 3-4: Strategy & Backtest
- ทำ PART 03 และ PART 04
- พัฒนากลยุทธ์ของตัวเอง
- Backtest และปรับแต่ง parameters

### Week 5-6: Risk & Portfolio
- ทำ PART 05 และ PART 06
- เข้าใจ risk management ลึกซึ้ง
- สร้าง multi-asset portfolio

### Week 7-8: Execution & Production
- ทำ PART 07, 08, 09
- เชื่อมต่อกับ exchange/broker
- Deploy และรัน paper trading

### Week 9+: Advanced & Live
- ทำ PART 10
- รัน paper trading 2-4 สัปดาห์
- Go live with micro capital

---

## 📚 เนื้อหาใน PART ต่างๆ (Quick Reference)

| PART | หัวข้อ | ขั้น | ความยาก | เวลา |
|------|--------|------|---------|------|
| [01](docs/PART01.md) | Setup & Basics | 1-10 | ⭐ | 2-3 วัน |
| [02](docs/PART02.md) | Data Feeders | 11-20 | ⭐⭐ | 3-4 วัน |
| [03](docs/PART03.md) | Strategy Design | 21-30 | ⭐⭐ | 4-5 วัน |
| [04](docs/PART04.md) | Backtesting | 31-40 | ⭐⭐⭐ | 5-7 วัน |
| [05](docs/PART05.md) | Risk Management | 41-50 | ⭐⭐⭐ | 4-5 วัน |
| [06](docs/PART06.md) | Portfolio | 51-60 | ⭐⭐⭐ | 4-5 วัน |
| [07](docs/PART07.md) | Execution | 61-70 | ⭐⭐⭐⭐ | 5-7 วัน |
| [08](docs/PART08.md) | Monitoring | 71-80 | ⭐⭐⭐ | 3-4 วัน |
| [09](docs/PART09.md) | Deployment | 81-90 | ⭐⭐⭐⭐ | 5-7 วัน |
| [10](docs/PART10.md) | Advanced | 91-100 | ⭐⭐⭐⭐⭐ | 7-10 วัน |

---

## 🎯 เริ่มต้นได้เลย!

พร้อมแล้วหรือยัง? เริ่มต้นด้วย:

### ⏭️ ขั้นตอนถัดไป

1. ✅ อ่าน [README.md](README.md) ให้จบ
2. ✅ อ่าน [SUMMARY.md](SUMMARY.md) สำหรับภาพรวม
3. ✅ ตรวจสอบ [CHECKLIST.md](CHECKLIST.md)
4. ▶️ **เริ่มต้นที่ [PART 01](docs/PART01.md)**

---

## 📝 บันทึกการเรียนรู้

แนะนำให้สร้าง **Learning Journal** เพื่อบันทึก:

```markdown
# My Learning Journal

## Week 1
- [x] Completed PART 01
- [x] Downloaded 3 years of data for 5 assets
- [ ] Issue: yfinance timeout sometimes → need retry logic

## Week 2
- [x] Completed PART 02
- [x] Built Yahoo and CCXT feeders
- Learned: Data normalization is crucial!

... ฯลฯ
```

---

## 🏆 เป้าหมายสุดท้าย

เมื่อทำครบ 100 ขั้นตอน คุณจะสามารถ:

- ✅ **สร้าง** trading bot ได้เอง จากศูนย์
- ✅ **Backtest** กลยุทธ์ได้อย่างถูกต้อง
- ✅ **Deploy** ขึ้น production ด้วย Docker
- ✅ **Monitor** และ maintain ระบบได้
- ✅ **เข้าใจ** algorithmic trading แบบลึกซึ้ง
- ✅ **ต่อยอด** พัฒนาฟีเจอร์ใหม่ๆ ได้

---

**มาเริ่มต้นกันเลย! 🚀**

👉 **[ไปที่ PART 01: พื้นฐานและตั้งค่าสภาพแวดล้อม](docs/PART01.md)**

---

*"The best time to start was yesterday. The next best time is now."*

**สร้างด้วย ❤️ โดย Trading Bot Development Team**

*Last Updated: 2024-01-15*
