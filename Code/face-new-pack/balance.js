const Matic = require('maticjs').default
const config = require('./config')

// Create object of Matic
const matic = new Matic({
  maticProvider: config.MATIC_PROVIDER,
  parentProvider: config.PARENT_PROVIDER,
  rootChainAddress: config.ROOTCHAIN_ADDRESS,
  syncerUrl: config.SYNCER_URL,
  watcherUrl: config.WATCHER_URL,
  maticWethAddress: config.MATICWETH_ADDRESS,
})
matic.wallet = config.PRIVATE_KEY // prefix with `0x`

const tokenAddress = config.MATIC_TEST_TOKEN // token address on mainchain
const from = config.FROM_ADDRESS // from address

matic.balanceOfERC20(from, tokenAddress, {
  // parent: true, // For token balance on Main network (false for Matic Network)
}).then((hash) => { 
  // action on Transaction success
  console.log(round(WeiToEth(hash),5)); // eslint-disable-line
})

////////utility functions////////

function round(value, decimals) {
    return Number(Math.round(value+'e'+decimals)+'e-'+decimals);
  }

function WeiToEth(wei) {
    return wei*0.000000000000000001;
  }