while(me.isAlive()){
    me.coding();
    if (me.getCode().haveProplem()) {
        Google.serch("How to do fix " + me.getCode().getProplem());
        me.openStackOverFlow();
        me.copyAnswer();
        me.getCode().paste();
        me.getCode().compile();
        me.getCode().run();
    }
}