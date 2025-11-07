# 📝 TODO - Current Sprint & Backlog

> รายการงานที่กำลังทำ รายการรอทำ และแผนการพัฒนา

**Last Updated**: 2024-01-15
**Current Sprint**: Sprint 3 (Backtesting Framework)
**Sprint Duration**: 2024-01-08 → 2024-01-22

---

## 🔥 This Week (High Priority)

### 🚀 In Progress

- [x] สร้างโครงสร้างโปรเจคพื้นฐาน
- [x] สร้าง configuration files (routing.yml, risk.yml, env.sample)
- [x] สร้าง README.md และ documentation
- [ ] **สร้าง base feeder class** (engine/feeders/base.py)
  - [ ] กำหนด abstract methods
  - [ ] กำหนด data normalization interface
  - [ ] สร้าง error handling base
  - **Assignee**: Development Team
  - **Due**: 2024-01-16

- [ ] **Yahoo Finance Feeder** (engine/feeders/yahoo.py)
  - [ ] ใช้ yfinance library
  - [ ] ดึงข้อมูล OHLCV
  - [ ] Handle missing data
  - [ ] Cache กับ Parquet
  - **Assignee**: Development Team
  - **Due**: 2024-01-17

- [ ] **CCXT Cryptocurrency Feeder** (engine/feeders/ccxt_live.py)
  - [ ] เชื่อมต่อ Binance
  - [ ] ดึงข้อมูล spot OHLCV
  - [ ] Handle rate limits
  - [ ] WebSocket support (optional)
  - **Assignee**: Development Team
  - **Due**: 2024-01-18

### 📋 Planned This Week

- [ ] **MA Crossover Strategy** (engine/strategy/ma_cross.py)
  - [ ] Simple MA crossover logic
  - [ ] Entry/exit signals
  - [ ] Parameter optimization
  - **Assignee**: Strategy Team
  - **Due**: 2024-01-19

- [ ] **VectorBT Basic Backtest** (engine/backtest/vectorbt_runner.py)
  - [ ] Setup VectorBT
  - [ ] Single strategy backtest
  - [ ] Generate performance metrics
  - **Assignee**: Quant Team
  - **Due**: 2024-01-20

---

## 📆 Next Week (Jan 22-28)

- [ ] MetaTrader 5 Feeder (Forex)
- [ ] RSI Mean Reversion Strategy
- [ ] Position Sizing Module
- [ ] Risk Guard Implementation
- [ ] Unit Tests for Feeders

---

## 🎯 Current Sprint Goals (Sprint 3)

**Sprint Theme**: Backtesting Foundation

**Sprint Goal**: มี working backtest สำหรับ MA strategy บน 3 assets

### Sprint Backlog

#### Data Layer
- [x] โครงสร้าง data/
- [ ] Base feeder class
- [ ] Yahoo feeder (Stocks/Commodities)
- [ ] CCXT feeder (Crypto)
- [ ] Data caching mechanism
- [ ] Data validation utilities

#### Strategy Layer
- [ ] Base strategy class
- [ ] MA Crossover strategy
- [ ] Signal generation framework
- [ ] Strategy parameter validation

#### Backtesting
- [ ] VectorBT integration
- [ ] Performance metrics calculation
- [ ] Equity curve plotting
- [ ] Basic backtest runner

#### Testing
- [ ] Unit tests: feeders
- [ ] Unit tests: strategy
- [ ] Integration test: end-to-end backtest

**Definition of Done**:
- [ ] Code merged to main
- [ ] Tests passing (coverage > 80%)
- [ ] Documentation updated
- [ ] Peer review completed

---

## 📚 Backlog (Prioritized)

### P0 - Critical (Must Have for MVP)

1. [ ] **Data Feeders - Core**
   - [ ] Yahoo Finance feeder
   - [ ] CCXT feeder (Binance)
   - [ ] Data normalization
   - [ ] Error handling & retry

2. [ ] **Basic Strategy**
   - [ ] MA Crossover
   - [ ] Entry/Exit logic
   - [ ] Signal validation

3. [ ] **Backtesting Framework**
   - [ ] VectorBT runner
   - [ ] Metrics calculation
   - [ ] Report generation

4. [ ] **Risk Management - Basic**
   - [ ] Position sizing (fixed %)
   - [ ] Max position limit
   - [ ] Daily loss limit

5. [ ] **Configuration**
   - [ ] Risk parameters
   - [ ] Asset routing
   - [ ] Environment variables

### P1 - High Priority (Should Have)

6. [ ] **MT5 Integration**
   - [ ] MT5 feeder
   - [ ] Forex data download
   - [ ] Order execution (future)

7. [ ] **Additional Strategies**
   - [ ] RSI Mean Reversion
   - [ ] Breakout Strategy
   - [ ] Multi-timeframe analysis

8. [ ] **Advanced Backtesting**
   - [ ] Walk-forward analysis
   - [ ] Parameter optimization
   - [ ] Monte Carlo simulation

9. [ ] **Risk Management - Advanced**
   - [ ] ATR-based sizing
   - [ ] Volatility targeting
   - [ ] Correlation checks
   - [ ] Circuit breakers

10. [ ] **Portfolio Management**
    - [ ] Multi-asset tracking
    - [ ] Portfolio optimizer
    - [ ] Rebalancing logic

### P2 - Medium Priority (Nice to Have)

11. [ ] **Paper Trading**
    - [ ] Simulated execution
    - [ ] Real-time data feeds
    - [ ] Performance tracking

12. [ ] **Order Execution**
    - [ ] CCXT order client
    - [ ] MT5 order client
    - [ ] Order management system

13. [ ] **Monitoring**
    - [ ] Prometheus metrics
    - [ ] Grafana dashboards
    - [ ] Alert system

14. [ ] **Database**
    - [ ] PostgreSQL setup
    - [ ] Schema design
    - [ ] Trade/order logging

15. [ ] **Web API**
    - [ ] FastAPI backend
    - [ ] REST endpoints
    - [ ] Authentication

### P3 - Low Priority (Future)

16. [ ] **Machine Learning**
    - [ ] Feature engineering
    - [ ] ML models
    - [ ] Online learning

17. [ ] **Advanced Features**
    - [ ] Multi-venue arbitrage
    - [ ] Options trading
    - [ ] Derivatives support

18. [ ] **Mobile App**
    - [ ] React Native app
    - [ ] Push notifications
    - [ ] Mobile dashboard

---

## 🐛 Bugs & Issues

### 🔴 Critical

_(ไม่มีในขณะนี้)_

### 🟡 High

_(ไม่มีในขณะนี้)_

### 🟢 Medium

_(ไม่มีในขณะนี้)_

### 🔵 Low

_(ไม่มีในขณะนี้)_

---

## 💡 Technical Debt

### Code Quality

- [ ] Add type hints ให้ครบทุกฟังก์ชัน
- [ ] Refactor duplicated code
- [ ] Improve error messages
- [ ] Add docstrings ให้ครบ

### Testing

- [ ] เพิ่ม test coverage > 90%
- [ ] Add integration tests
- [ ] Add performance tests
- [ ] Mock external API calls

### Documentation

- [ ] Complete API documentation
- [ ] Add more code examples
- [ ] Create video tutorials
- [ ] Translate docs to English

### Infrastructure

- [ ] Setup CI/CD pipeline
- [ ] Automated testing
- [ ] Automated deployment
- [ ] Performance monitoring

---

## 🎨 Nice to Have (Ideas)

### Features

- [ ] TradingView webhook integration
- [ ] Discord bot สำหรับ alerts
- [ ] Telegram bot สำหรับควบคุม
- [ ] Voice alerts สำหรับ critical events
- [ ] Strategy marketplace
- [ ] Community backtests sharing

### Improvements

- [ ] Dark mode สำหรับ dashboard
- [ ] Multi-language support
- [ ] Custom indicator builder
- [ ] Visual strategy builder
- [ ] Drag-and-drop portfolio builder

### Integrations

- [ ] TradingView integration
- [ ] MetaTrader integration
- [ ] Interactive Brokers
- [ ] TD Ameritrade
- [ ] Robinhood API

---

## 🚫 Won't Do / Cancelled

- ~~Real-time news sentiment analysis~~ - Too complex for MVP
- ~~High-frequency trading~~ - Out of scope
- ~~Social trading features~~ - Focus on individual trading
- ~~Cryptocurrency mining~~ - Not related to trading

---

## 📊 Sprint Velocity & Metrics

### Sprint 1 (Dec 18-31, 2023)
- **Planned**: 15 story points
- **Completed**: 12 story points
- **Velocity**: 12
- **Completion Rate**: 80%

### Sprint 2 (Jan 1-7, 2024)
- **Planned**: 12 story points
- **Completed**: 10 story points
- **Velocity**: 10
- **Completion Rate**: 83%

### Sprint 3 (Jan 8-22, 2024) - Current
- **Planned**: 13 story points
- **Completed**: 5 story points (so far)
- **Target Velocity**: 12
- **Status**: On track

---

## 🎯 Quarter Goals (Q1 2024)

### January
- [x] โครงสร้างโปรเจคเสร็จ
- [x] Documentation framework เสร็จ
- [ ] Data feeders เสร็จ
- [ ] Basic strategy + backtest เสร็จ

### February
- [ ] Advanced backtesting (Walk-forward, Monte Carlo)
- [ ] Risk management เสร็จ
- [ ] Portfolio management เสร็จ
- [ ] Paper trading พร้อม

### March
- [ ] Live execution engine
- [ ] Monitoring & alerts
- [ ] Production deployment
- [ ] 2 สัปดาห์ paper trading สำเร็จ

---

## 🔄 Recurring Tasks

### Daily
- [ ] Check system health (ถ้ารัน live)
- [ ] Review logs
- [ ] Monitor performance
- [ ] Update TODO list

### Weekly
- [ ] Sprint planning (Monday)
- [ ] Code review session (Wednesday)
- [ ] Sprint retrospective (Friday)
- [ ] Update dependencies
- [ ] Backup data

### Monthly
- [ ] Security audit
- [ ] Performance review
- [ ] Cost analysis
- [ ] Strategy review
- [ ] Update roadmap

---

## 📝 Meeting Notes & Decisions

### 2024-01-15: Sprint Planning

**Attendees**: Development Team

**Decisions**:
1. เลือก VectorBT เป็น primary backtest framework
2. เริ่มจาก Yahoo + CCXT feeders ก่อน, MT5 ทำทีหลัง
3. MA Crossover เป็น strategy แรก
4. Target: MVP พร้อมภายในสิ้น Q1 2024

**Action Items**:
- [x] สร้าง config files
- [x] สร้าง documentation
- [ ] เริ่มพัฒนา data feeders

---

## 🏆 Milestones

### Milestone 1: Foundation ✅ (Completed 2024-01-10)
- [x] Project structure
- [x] Configuration system
- [x] Documentation framework

### Milestone 2: Data Layer 🔄 (Target: 2024-01-25)
- [ ] Yahoo feeder
- [ ] CCXT feeder
- [ ] Data caching
- [ ] Unit tests

### Milestone 3: Strategy & Backtest 📋 (Target: 2024-02-10)
- [ ] MA Crossover strategy
- [ ] VectorBT integration
- [ ] Performance metrics
- [ ] Reports

### Milestone 4: Risk & Portfolio 📋 (Target: 2024-02-25)
- [ ] Position sizing
- [ ] Risk guards
- [ ] Portfolio manager
- [ ] Advanced backtesting

### Milestone 5: Paper Trading 📋 (Target: 2024-03-15)
- [ ] Paper trading mode
- [ ] Monitoring
- [ ] Alerts
- [ ] 2 weeks successful run

### Milestone 6: Production Ready 📋 (Target: 2024-03-31)
- [ ] Live execution engine
- [ ] Full monitoring stack
- [ ] Security audit
- [ ] Micro capital live test

---

## 📞 Who's Working on What

| Person | Current Task | Status | ETA |
|--------|-------------|--------|-----|
| Lead Dev | Base feeder class | 🔄 In Progress | Jan 16 |
| Dev 1 | Yahoo feeder | 📋 Planned | Jan 17 |
| Dev 2 | CCXT feeder | 📋 Planned | Jan 18 |
| Quant | Strategy design | 📋 Planned | Jan 19 |

---

## 🎓 Learning & Research

### To Learn
- [ ] VectorBT advanced features
- [ ] Walk-forward optimization techniques
- [ ] Monte Carlo simulation best practices
- [ ] Risk parity portfolio construction

### Reading List
- [ ] "Advances in Financial Machine Learning" - Marcos López de Prado
- [ ] "Algorithmic Trading" - Ernest P. Chan
- [ ] "Quantitative Trading" - Ernest P. Chan
- [ ] VectorBT documentation

### Courses
- [ ] Udemy: Algorithmic Trading with Python
- [ ] Coursera: Machine Learning for Trading
- [ ] QuantInsti: Executive Programme in Algorithmic Trading

---

## 💭 Notes & Ideas

### Strategy Ideas
- Momentum + Mean Reversion combo
- Regime-switching strategies
- Sector rotation (stocks)
- Carry trade (Forex)
- Funding rate arbitrage (Crypto)

### Technical Improvements
- WebSocket real-time data
- Distributed backtesting (multi-core)
- GPU-accelerated backtesting
- Automated parameter optimization
- Strategy ensemble methods

### Risk Improvements
- Dynamic position sizing based on VIX
- Portfolio heat map visualization
- Tail risk hedging
- Stress testing framework
- Black swan scenario planning

---

## ✅ Recently Completed (Last 2 Weeks)

- [x] สร้างโครงสร้างโปรเจคทั้งหมด (2024-01-08)
- [x] สร้าง requirements.txt (2024-01-09)
- [x] สร้าง config files (routing.yml, risk.yml) (2024-01-10)
- [x] สร้าง README.md ครบถ้วน (2024-01-12)
- [x] สร้าง SUMMARY.md (2024-01-13)
- [x] สร้าง TASK.md (2024-01-14)
- [x] สร้าง CHECKLIST.md (2024-01-15)
- [x] สร้าง TODO.md (2024-01-15)

---

## 🔮 Long-term Vision (2024-2025)

### Q2 2024
- Production-grade live trading
- Multiple strategies running
- Full monitoring & analytics
- Mobile app beta

### Q3 2024
- Machine learning integration
- Advanced portfolio optimization
- Multi-venue support
- API marketplace

### Q4 2024
- Options & derivatives
- Institutional-grade features
- White-label solution
- Community platform

### 2025
- Hedge fund-level infrastructure
- Distributed trading network
- AI-powered strategy generation
- Global expansion

---

**Last Reviewed**: 2024-01-15
**Next Review**: 2024-01-22 (Weekly)

**Remember**:
- Break down large tasks
- Update TODO regularly
- Celebrate small wins
- Ask for help when stuck
- Keep learning & improving

---

> "The secret to getting ahead is getting started." - Mark Twain

🚀 Let's build something amazing!
