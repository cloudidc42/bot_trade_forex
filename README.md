# 🤖 Multi-Asset Algorithmic Trading Bot System

> ระบบเทรดอัตโนมัติแบบครบวงจรสำหรับหลายสินทรัพย์: Forex, Bitcoin-Crypto, หุ้น, ทอง, และน้ำมัน

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Development-yellow.svg)](https://github.com)

---

## 📋 สารบัญ

- [ภาพรวม](#ภาพรวม)
- [คุณสมบัติหลัก](#คุณสมบัติหลัก)
- [สถาปัตยกรรม](#สถาปัตยกรรม)
- [สินทรัพย์ที่รองรับ](#สินทรัพย์ที่รองรับ)
- [ติดตั้งและเริ่มต้น](#ติดตั้งและเริ่มต้น)
- [การใช้งาน](#การใช้งาน)
- [โครงสร้างโปรเจค](#โครงสร้างโปรเจค)
- [Documentation](#documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 ภาพรวม

ระบบ Multi-Asset Trading Bot นี้เป็นแพลตฟอร์มการเทรดอัตโนมัติแบบ end-to-end ที่ครอบคลุมตั้งแต่:

- **Research** - วิเคราะห์และทดสอบไอเดียกลยุทธ์
- **Backtest** - ทดสอบย้อนหลังด้วยข้อมูลประวัติศาสตร์
- **Paper Trading** - ทดสอบด้วยเงินจำลองแบบ real-time
- **Live Trading** - เทรดจริงด้วยระบบอัตโนมัติ
- **Monitoring** - ติดตามและแจ้งเตือนตลอด 24/7

### 🎓 เป้าหมาย

โปรเจคนี้สร้างขึ้นเพื่อ:

1. **เรียนรู้** - ทำความเข้าใจการสร้างระบบเทรดแบบมืออาชีพ
2. **ปฏิบัติได้จริง** - รันได้ทันทีพร้อม config ครบถ้วน
3. **ขยายได้** - สถาปัตยกรรมยืดหยุ่นและปรับแต่งง่าย
4. **Production-Ready** - มี monitoring, logging, และ risk management

---

## ✨ คุณสมบัติหลัก

### 📊 Data & Market Access

- ✅ **Crypto**: Binance, Coinbase, FTX (via CCXT)
- ✅ **Forex**: MetaTrader 5 integration
- ✅ **Stocks**: Yahoo Finance, Alpaca
- ✅ **Commodities**: Gold (GLD), Oil (USO), Silver (SLV) via ETFs

### 🧠 Strategy Framework

- ✅ Moving Average Crossover
- ✅ RSI Mean Reversion
- ✅ Breakout Strategy
- ✅ Multi-timeframe analysis
- ✅ Regime detection (Trend/Range)
- ✅ Custom indicator library (pandas_ta, ta)

### 🎯 Backtesting

- ✅ **VectorBT** - High-performance vectorized backtesting
- ✅ **Backtrader** - Event-driven backtesting
- ✅ **FreqTrade** - Crypto-focused backtesting
- ✅ Walk-forward analysis
- ✅ Monte Carlo simulation
- ✅ Multi-asset portfolio backtesting

### 🛡️ Risk Management

- ✅ Position sizing (ATR-based, volatility targeting)
- ✅ Portfolio-level limits (max drawdown, daily loss)
- ✅ Asset class exposure limits
- ✅ Correlation-aware position management
- ✅ Circuit breakers
- ✅ Dynamic position adjustment

### 📈 Execution & Routing

- ✅ Multi-broker/exchange support
- ✅ Smart order routing
- ✅ Slippage modeling
- ✅ Fee calculation
- ✅ Order validation
- ✅ Retry logic with exponential backoff

### 🔍 Monitoring & Observability

- ✅ Prometheus metrics
- ✅ Grafana dashboards
- ✅ Loki log aggregation
- ✅ Real-time alerts (Telegram, Email)
- ✅ Performance reporting
- ✅ Trade journal

### 🐳 Infrastructure

- ✅ Docker containerization
- ✅ Docker Compose orchestration
- ✅ PostgreSQL database
- ✅ Automated backups
- ✅ CI/CD with GitHub Actions

---

## 🏗️ สถาปัตยกรรม

```
┌──────────────────────────────────────────────────────────────────┐
│                        Trading Bot System                         │
└──────────────────────────────────────────────────────────────────┘

        ┌──────────────┐      OHLCV/ticks      ┌──────────────┐
        │  Feeders     │◄──────────────────────│  Exchanges   │
        │ (Yahoo,CCXT, │                       │/Brokers (MT5)│
        │     MT5)     │                       │              │
        └──────┬───────┘                       └──────┬───────┘
               │   signals/metrics                    │ orders/trades
               ▼                                       ▼
        ┌──────────────┐    sizing/risk     ┌──────────────┐
        │  Strategy    │────────────────────►│  Portfolio   │
        │   Engine     │                    │   Manager    │
        └──────┬───────┘                    └──────┬───────┘
               │ backtest/live                      │ route per asset
               ▼                                     ▼
        ┌──────────────┐ metrics/logs ┌──────────────┐
        │  Backtest    │──────────────►│ Monitoring   │
        │   Engine     │               │(Prom/Grafana)│
        └──────┬───────┘               └──────┬───────┘
               │ reports                           │ alerts
               ▼                                   ▼
        ┌──────────────┐                    ┌──────────────┐
        │   Reports    │                    │   Web/API     │
        │   Generator  │                    │   Dashboard   │
        └──────────────┘                    └──────────────┘
```

### 🔄 Data Flow

1. **Market Data** → Feeders ดึงข้อมูล OHLCV/Tick จาก exchanges/brokers
2. **Strategy** → วิเคราะห์และสร้างสัญญาณเทรด
3. **Risk Management** → ตรวจสอบและอนุมัติตามกฎความเสี่ยง
4. **Portfolio** → คำนวณขนาดตำแหน่งและจัดการพอร์ต
5. **Execution** → Route orders ไปยัง broker/exchange ที่เหมาะสม
6. **Monitoring** → บันทึก metrics และส่ง alerts

---

## 🎯 สินทรัพย์ที่รองรับ

### 1. 💰 Cryptocurrency (Crypto)

| Symbol | Name | Exchange | Type |
|--------|------|----------|------|
| BTC/USDT | Bitcoin | Binance | Spot |
| ETH/USDT | Ethereum | Binance | Spot |
| BTC/USDT:USDT | Bitcoin Futures | Binance | Perpetual |

### 2. 💱 Foreign Exchange (Forex)

| Symbol | Name | Broker | Leverage |
|--------|------|--------|----------|
| EURUSD | Euro vs US Dollar | MT5 | 1:30 |
| GBPUSD | Pound vs US Dollar | MT5 | 1:30 |
| USDJPY | US Dollar vs Yen | MT5 | 1:30 |

### 3. 📈 Stocks & ETFs

| Symbol | Name | Exchange | Type |
|--------|------|----------|------|
| AAPL | Apple Inc. | NASDAQ | Stock |
| TSLA | Tesla Inc. | NASDAQ | Stock |
| SPY | S&P 500 ETF | NYSE | ETF |

### 4. 🏆 Commodities

| Symbol | Name | Type | Feeder |
|--------|------|------|--------|
| GLD | Gold ETF | ETF | Yahoo Finance |
| USO | US Oil Fund | ETF | Yahoo Finance |
| SLV | Silver ETF | ETF | Yahoo Finance |

---

## 🚀 ติดตั้งและเริ่มต้น

### ข้อกำหนดเบื้องต้น (Prerequisites)

- Python 3.11+
- Docker & Docker Compose
- Git
- 4GB RAM ขึ้นไป
- MetaTrader 5 (สำหรับ Forex - optional)

### 📥 Installation

#### 1. Clone Repository

```bash
git clone https://github.com/yourusername/bot_trade_forex.git
cd bot_trade_forex
```

#### 2. สร้าง Virtual Environment

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### 3. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

#### 4. ตั้งค่า Environment Variables

```bash
# คัดลอก template
cp configs/env.sample .env

# แก้ไขค่าใน .env
nano .env  # หรือใช้ text editor ที่ชอบ
```

**สิ่งที่ต้องกรอกใน `.env`:**

- API Keys สำหรับ exchanges (Binance, Coinbase, etc.)
- MT5 credentials (ถ้าเทรด Forex)
- Database credentials
- Telegram bot token (สำหรับ alerts)

#### 5. ตั้งค่า Database (Optional)

```bash
# ถ้าใช้ PostgreSQL
docker-compose up -d postgres

# ถ้าใช้ SQLite (ไม่ต้องทำอะไร - auto-create)
```

---

## 💻 การใช้งาน

### 🔬 1. Research & Data Exploration

```bash
# ดาวน์โหลดข้อมูลสำหรับ backtesting
python research/download_data.py --symbols AAPL,TSLA,GLD --period 3y

# Jupyter notebook สำหรับ analysis
jupyter notebook research/notebooks/alpha_research.ipynb
```

### 📊 2. Backtesting

```bash
# Backtest กลยุทธ์ MA Crossover
python -m engine.backtest.run_backtest \
  --strategy ma_cross \
  --symbols BTC/USDT,ETH/USDT \
  --start 2020-01-01 \
  --end 2023-12-31

# Backtest หลายกลยุทธ์พร้อมกัน
python -m engine.backtest.multi_strategy_backtest
```

**ผลลัพธ์:**

- CSV reports ใน `reports/backtest/`
- Equity curves, drawdown charts
- Performance metrics (Sharpe, Sortino, MaxDD, etc.)

### 🧪 3. Paper Trading

```bash
# เปิดโหมด paper trading
ENV=paper python -m engine.live.trader

# หรือใช้ Docker
docker-compose up -d trader-paper
```

### 🔴 4. Live Trading

⚠️ **คำเตือน: ใช้เงินจริง - ตรวจสอบ config ให้ดีก่อนรัน!**

```bash
# ตรวจสอบ risk limits
cat configs/risk.yml

# รัน live (ระวัง!)
ENV=live python -m engine.live.trader

# หรือใช้ Docker
docker-compose up -d trader-live
```

### 📈 5. Monitoring

```bash
# เปิด Grafana dashboard
docker-compose up -d monitoring

# เข้าถึง:
# Grafana: http://localhost:3000 (admin/admin)
# Prometheus: http://localhost:9090
```

**Dashboards:**

- Portfolio Performance
- Order Execution Metrics
- Risk Metrics
- System Health

### 📝 6. Generate Reports

```bash
# รายงานสรุปประจำวัน
python -m engine.reports.daily_report

# รายงานประจำเดือน
python -m engine.reports.monthly_report --month 2024-01
```

---

## 📂 โครงสร้างโปรเจค

```
bot_trade_forex/
│
├── configs/                    # Configuration files
│   ├── env.sample             # Environment variables template
│   ├── routing.yml            # Asset routing configuration
│   └── risk.yml               # Risk management rules
│
├── data/                      # Data storage
│   ├── raw/                   # Raw market data
│   └── processed/             # Processed/cached data
│
├── research/                  # Research & analysis
│   ├── notebooks/             # Jupyter notebooks
│   │   └── alpha_research.ipynb
│   ├── factors/               # Factor/indicator research
│   └── download_data.py       # Data download scripts
│
├── engine/                    # Core trading engine
│   ├── feeders/               # Market data feeders
│   │   ├── yahoo.py           # Yahoo Finance feeder
│   │   ├── ccxt_live.py       # CCXT crypto feeder
│   │   └── mt5.py             # MetaTrader 5 feeder
│   │
│   ├── strategy/              # Trading strategies
│   │   ├── base.py            # Base strategy class
│   │   ├── ma_cross.py        # MA crossover strategy
│   │   ├── meanrev.py         # Mean reversion strategy
│   │   └── breakout.py        # Breakout strategy
│   │
│   ├── portfolio/             # Portfolio management
│   │   ├── sizing.py          # Position sizing
│   │   ├── risk_guard.py      # Risk validation
│   │   └── router.py          # Order routing
│   │
│   ├── backtest/              # Backtesting framework
│   │   ├── vectorbt_runner.py # VectorBT engine
│   │   ├── bt_runner.py       # Backtrader engine
│   │   └── metrics.py         # Performance metrics
│   │
│   └── live/                  # Live trading
│       ├── trader.py          # Main trading loop
│       ├── order_client.py    # Order execution
│       └── health.py          # Health checks
│
├── web/                       # Web interface
│   ├── api.py                 # FastAPI backend
│   └── ui/                    # Frontend (optional)
│
├── monitoring/                # Monitoring stack
│   ├── prometheus.yml         # Prometheus config
│   └── grafana/               # Grafana dashboards
│       └── dashboards.json
│
├── docker/                    # Docker configuration
│   ├── Dockerfile
│   └── compose.yml
│
├── tests/                     # Unit & integration tests
│   ├── test_feeders.py
│   ├── test_strategy.py
│   ├── test_risk.py
│   └── test_router.py
│
├── docs/                      # Documentation
│   ├── TUTORIAL.md            # Step-by-step tutorial (100 steps)
│   ├── PART01.md              # Part 1: Setup (Steps 1-10)
│   ├── PART02.md              # Part 2: Data Feeders (Steps 11-20)
│   ├── ... (PART03-10)
│   ├── TASK.md                # Task list
│   ├── CHECKLIST.md           # Production checklist
│   └── TODO.md                # Todo items
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── SUMMARY.md                 # Project summary
└── LICENSE                    # License file
```

---

## 📚 Documentation

เอกสารครบถ้วนสำหรับการเรียนรู้และพัฒนา:

### 🎓 Tutorial & Learning Path

- **[TUTORIAL.md](docs/TUTORIAL.md)** - คู่มือหลัก (ภาพรวม 100+ ขั้นตอน)

### 📖 Step-by-Step Guides (แบ่งเป็น 10 ส่วน)

1. **[PART01.md](docs/PART01.md)** - พื้นฐานและตั้งค่าสภาพแวดล้อม (ขั้นที่ 1-10)
2. **[PART02.md](docs/PART02.md)** - Data Feeders และ Market Data (ขั้นที่ 11-20)
3. **[PART03.md](docs/PART03.md)** - Strategy Design พื้นฐาน (ขั้นที่ 21-30)
4. **[PART04.md](docs/PART04.md)** - Backtesting Framework (ขั้นที่ 31-40)
5. **[PART05.md](docs/PART05.md)** - Risk Management & Position Sizing (ขั้นที่ 41-50)
6. **[PART06.md](docs/PART06.md)** - Portfolio & Routing (ขั้นที่ 51-60)
7. **[PART07.md](docs/PART07.md)** - Order Execution & Broker Integration (ขั้นที่ 61-70)
8. **[PART08.md](docs/PART08.md)** - Monitoring & Observability (ขั้นที่ 71-80)
9. **[PART09.md](docs/PART09.md)** - Deployment & Production (ขั้นที่ 81-90)
10. **[PART10.md](docs/PART10.md)** - Advanced Topics & Optimization (ขั้นที่ 91-100)

### 📋 Management & Tracking

- **[SUMMARY.md](docs/SUMMARY.md)** - สรุปภาพรวมโปรเจค
- **[TASK.md](docs/TASK.md)** - รายการงานทั้งหมด
- **[CHECKLIST.md](docs/CHECKLIST.md)** - Production readiness checklist
- **[TODO.md](docs/TODO.md)** - สิ่งที่ต้องทำ/กำลังทำ

---

## 🧪 Testing

### Unit Tests

```bash
# รัน all tests
pytest tests/

# รัน specific test
pytest tests/test_strategy.py -v

# รันพร้อม coverage
pytest --cov=engine tests/
```

### Integration Tests

```bash
# ทดสอบการเชื่อมต่อ exchange
python tests/integration/test_exchange_connection.py

# ทดสอบ end-to-end workflow
python tests/integration/test_e2e_workflow.py
```

### Backtest Validation

```bash
# Validate backtest results
python tests/validate_backtest_metrics.py
```

---

## 🐳 Deployment

### Development

```bash
docker-compose -f docker/compose.yml up -d
```

### Production

```bash
# Build production images
docker-compose -f docker/compose.prod.yml build

# Deploy
docker-compose -f docker/compose.prod.yml up -d

# Check logs
docker-compose logs -f trader
```

### Kubernetes (Advanced)

```bash
# Apply configurations
kubectl apply -f k8s/

# Check pods
kubectl get pods -n trading-bot
```

---

## 🔧 Configuration

### Risk Parameters

แก้ไข `configs/risk.yml`:

```yaml
portfolio:
  max_daily_loss_pct: 2.0  # ขาดทุนสูงสุด 2% ต่อวัน
  max_position_size_pct: 5.0  # ขนาดตำแหน่งสูงสุด 5%
```

### Asset Routing

แก้ไข `configs/routing.yml`:

```yaml
crypto:
  - symbol: BTC/USDT
    exchange: binance
    fee_maker: 0.001
```

---

## ⚠️ คำเตือนและข้อควรระวัง

### 🚨 Risk Warnings

1. **การเทรดมีความเสี่ยง** - อาจสูญเสียเงินทุนทั้งหมด
2. **ทดสอบก่อนใช้จริง** - รัน paper trading อย่างน้อย 1-2 สัปดาห์
3. **ตรวจสอบ config** - ดู risk limits และ API keys ก่อนรัน live
4. **Backup ข้อมูล** - สำรองฐานข้อมูลและ config เป็นประจำ
5. **Monitor อย่างใกล้ชิด** - ติดตาม logs และ metrics ตลอดเวลา

### 🔐 Security Best Practices

- ❌ **ห้าม** commit API keys ลง Git
- ✅ ใช้ `.env` file และเพิ่มใน `.gitignore`
- ✅ ใช้ API keys ที่มี read-only permission สำหรับ backtest
- ✅ จำกัด withdrawal permission บน API keys
- ✅ ใช้ IP whitelist ถ้า exchange รองรับ
- ✅ เปิด 2FA บนทุก exchange/broker account

---

## 🤝 Contributing

เรายินดีรับ contributions! กรุณาอ่าน [CONTRIBUTING.md](CONTRIBUTING.md) ก่อน submit PR

### Development Workflow

1. Fork repository
2. สร้าง feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

---

## 📞 Support & Community

- 📧 Email: support@tradingbot.example.com
- 💬 Discord: [Join our community](https://discord.gg/tradingbot)
- 🐦 Twitter: [@TradingBotPro](https://twitter.com/tradingbotpro)
- 📖 Wiki: [GitHub Wiki](https://github.com/yourusername/bot_trade_forex/wiki)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [VectorBT](https://vectorbt.dev/) - High-performance backtesting
- [CCXT](https://github.com/ccxt/ccxt) - Cryptocurrency exchange library
- [MetaTrader5](https://www.metatrader5.com/) - Forex trading platform
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Prometheus](https://prometheus.io/) & [Grafana](https://grafana.com/) - Monitoring stack

---

## 📈 Project Status & Roadmap

### ✅ Phase 1: Foundation (Completed)
- [x] Project structure
- [x] Configuration system
- [x] Data feeders (Yahoo, CCXT, MT5)
- [x] Basic strategies (MA Cross, RSI)

### 🔄 Phase 2: Backtesting (In Progress)
- [x] VectorBT integration
- [x] Backtrader integration
- [ ] Walk-forward analysis
- [ ] Monte Carlo simulation

### 📋 Phase 3: Live Trading (Planned)
- [ ] Paper trading mode
- [ ] Live execution engine
- [ ] Order management system
- [ ] Trade reconciliation

### 🚀 Phase 4: Advanced Features (Future)
- [ ] Machine learning strategies
- [ ] Multi-venue arbitrage
- [ ] Options & derivatives support
- [ ] Mobile app

---

## 💡 Quick Start Examples

### Example 1: Simple Backtest

```python
from engine.backtest.vectorbt_runner import run_ma
import yfinance as yf

# ดาวน์โหลดข้อมูล
df = yf.download("GLD", period="3y", interval="1d")

# รัน MA crossover backtest
stats = run_ma(df, fast=20, slow=50, fees=0.001)
print(stats)
```

### Example 2: Live Paper Trading

```python
from engine.live.trader import TradingBot
import os

# ตั้งค่า environment
os.environ['ENV'] = 'paper'

# สร้าง bot instance
bot = TradingBot(
    strategy='ma_cross',
    symbols=['BTC/USDT', 'ETH/USDT'],
    timeframe='1h'
)

# รัน bot
bot.run()
```

---

**สร้างด้วย ❤️ โดยทีม Trading Bot Development**

*หมายเหตุ: ระบบนี้สร้างขึ้นเพื่อการศึกษาและวิจัย ผู้ใช้ต้องรับผิดชอบความเสี่ยงทางการเงินด้วยตนเอง*
