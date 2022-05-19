while(me.isAlive()){
    me.startCoding();
    try {
        me.getCode().compile();
        me.getCode().run();
    } catch (Exception e) {
        Google.serch("How to do fix " + me.getCode().getProplem());
        me.openStackOverFlow();
        me.copyAnswer();
        me.getCode().paste();
    }
}