const userName = 'ssafy'

if (userName === '1q2w3e4r') {
  message = '<h1> THIS IS ADMIN PAGE</h1>'
} else if (userName === 'ssafy') {
  message = '<h1>You r from SSAFY!</h1>'
} else {
  message = `<h1>hello ${userName} </h1>`
}

//switch

switch (userName) {
  case '1q2w3e4r': {
    message = '<h1>this is Admin</h1>'
  }
  case 'ssafy': {
    message = '<h1>you r from SSAFY</h1>'
  }
  default: {
    message = `<h1>hello ${userName} </h1>`
  }
}

